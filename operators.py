import variable
from tokenizer import TOKENS, Token


def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def isTrue(token):
    val = False
    if token.type == TOKENS.INTEGER and isInt(token.value):
        if int(token.value) != 0:
            val = True
    elif token.type == TOKENS.FLOAT and isFloat(token.value):
        if float(token.value) != 0.0:
            val = True
    elif token.type == TOKENS.STRING and token.value:
        val = True
    elif token.type == TOKENS.BOOLEANTRUE:
        val = True
    return val


def replaceIdentifier(stack):
    value = stack.pop()
    if value.type == TOKENS.IDENTIFIER and value.value in variable.globalVariables:
        temp = variable.globalVariables[value.value]
        value.value = temp.strValue
        value.type = temp.type
        value.superType = TOKENS.VALUE
    return value


def binaryAdd(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)
    if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) + int(right.value)
        stack.append(Token(TOKENS.INTEGER, str(result), TOKENS.VALUE))
    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) + float(right.value)
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))
    elif (left.type == TOKENS.FLOAT and right.type == TOKENS.INTEGER) or (left.type == TOKENS.INTEGER and right.type == TOKENS.FLOAT):
        result = float(left.value) + float(right.value)
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))
    elif left.type == TOKENS.STRING and right.type == TOKENS.STRING:
        result = left.value + right.value
        stack.append(Token(TOKENS.STRING, result, TOKENS.VALUE))
    else:
        result = str(left.value) + str(right.value)
        stack.append(Token(TOKENS.STRING, result, TOKENS.VALUE))


def Assingment(stack):
    right = replaceIdentifier(stack)
    name = stack.pop()

    var = variable.Variable(name.value)
    var.superType = right.superType

    if right.type == TOKENS.INTEGER:
        var.type = TOKENS.INTEGER
        var.intValue = int(right.value)

    elif right.type == TOKENS.FLOAT:
        var.type = TOKENS.FLOAT
        var.floatValue = float(right.value)

    elif right.type == TOKENS.STRING:
        var.type = TOKENS.STRING
        var.strValue = right.value

    elif right.type == TOKENS.BOOLEANTRUE:
        var.type = TOKENS.BOOLEANTRUE
        var.strValue = int(right.value)

    elif right.type == TOKENS.BOOLEANFALSE:
        var.type = TOKENS.BOOLEANFALSE
        var.strValue = int(right.value)

    var.update()
    variable.globalVariables[name.value] = var
    stack.append(Token(var.type, var.strValue, var.superType))


def unaryNegation(stack):
    value = replaceIdentifier(stack)

    if value.type == TOKENS.INTEGER:
        value.value = str(-int(value.value))

    elif value.type == TOKENS.FLOAT:
        value.value = str(-float(value.value))

    else:
        value.value = 'Error'
        value.type = TOKENS.STRING
    stack.append(value)


def binarySubtraction(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) - int(right.value)
        stack.append(Token(TOKENS.INTEGER, str(result), TOKENS.VALUE))
    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) - float(right.value)
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))
    elif (left.type == TOKENS.FLOAT and right.type == TOKENS.INTEGER) or (left.type == TOKENS.INTEGER and right.type == TOKENS.FLOAT):
        result = float(left.value) - float(right.value)
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))
    else:
        result = 'Error'
        stack.append(Token(TOKENS.STRING, result, TOKENS.VALUE))


def binaryMultiply(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) * int(right.value)
        stack.append(Token(TOKENS.INTEGER, str(result), TOKENS.VALUE))
    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) * float(right.value)
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))
    elif (left.type == TOKENS.FLOAT and right.type == TOKENS.INTEGER) or (left.type == TOKENS.INTEGER and right.type == TOKENS.FLOAT):
        result = float(left.value) * float(right.value)
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))
    else:
        result = 'Error'
        stack.append(Token(TOKENS.STRING, result, TOKENS.VALUE))


def binaryDivision(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    try:

        if (right.type == TOKENS.INTEGER and int(right.value) == 0) or (right.type == TOKENS.FLOAT and float(right.value) == 0.0):
            stack.append(Token(TOKENS.STRING, 'Error', TOKENS.VALUE))
            return

        left_value = float(left.value) if left.type in [
            TOKENS.INTEGER, TOKENS.FLOAT] else 0.0
        right_value = float(right.value) if right.type in [
            TOKENS.INTEGER, TOKENS.FLOAT] else 0.0

        result = left_value / right_value
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))

    except ZeroDivisionError:
        stack.append(Token(TOKENS.STRING, 'Error', TOKENS.VALUE))


def binaryAND(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    logicalLeft = isTrue(left)
    logicalRight = isTrue(right)

    result = logicalLeft and logicalRight
    if result:
        stack.append(Token(TOKENS.BOOLEANTRUE,
                     TOKENS.BOOLEANTRUE, TOKENS.VALUE))
    else:
        stack.append(Token(TOKENS.BOOLEANFALSE,
                     TOKENS.BOOLEANFALSE, TOKENS.VALUE))


def binaryOR(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    logicalLeft = isTrue(left)
    logicalRight = isTrue(right)

    result = logicalLeft or logicalRight
    if result:
        stack.append(Token(TOKENS.BOOLEANTRUE,
                     TOKENS.BOOLEANTRUE, TOKENS.VALUE))
    else:
        stack.append(Token(TOKENS.BOOLEANFALSE,
                     TOKENS.BOOLEANFALSE, TOKENS.VALUE))


def binaryNotEqual(stack):
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)

    # Strictly String Case:
    if lhs.type == TOKENS.STRING and rhs.type == TOKENS.STRING:
        result = lhs.value != rhs.value
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Integer Case:
    elif lhs.type == TOKENS.INTEGER and rhs.type == TOKENS.INTEGER:
        result = int(lhs.value) != int(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Float Case:
    elif lhs.type == TOKENS.FLOAT and rhs.type == TOKENS.FLOAT:
        result = float(lhs.value) != float(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Logical Case:
    elif (lhs.type == TOKENS.BOOLEANTRUE or lhs.type == TOKENS.BOOLEANFALSE) and \
            (rhs.type == TOKENS.BOOLEANTRUE or rhs.type == TOKENS.BOOLEANFALSE):
        result = rhs.type != lhs.type
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Mixed Cases:
        # int float
    elif (lhs.type == TOKENS.INTEGER or lhs.type == TOKENS.FLOAT) and \
            (rhs.type == TOKENS.INTEGER or rhs.type == TOKENS.FLOAT):
        result = float(lhs.value) != float(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # int string
    elif (lhs.type == TOKENS.INTEGER or lhs.type == TOKENS.STRING) and \
            (rhs.type == TOKENS.STRING or rhs.type == TOKENS.INTEGER):
        result = str(lhs.value) != str(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # float string
    elif (lhs.type == TOKENS.FLOAT or lhs.type == TOKENS.STRING) and \
            (rhs.type == TOKENS.STRING or rhs.type == TOKENS.FLOAT):
        result = str(lhs.value) != str(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # logical int
    elif (lhs.type == TOKENS.INTEGER or lhs.type == TOKENS.BOOLEANTRUE or lhs.type == TOKENS.BOOLEANFALSE) and \
            (rhs.type == TOKENS.INTEGER or rhs.type == TOKENS.BOOLEANTRUE or rhs.type == TOKENS.BOOLEANFALSE):
        result = not (isTrue(lhs)) or not (isTrue(rhs))
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # logical float
    elif (lhs.type == TOKENS.FLOAT or lhs.type == TOKENS.BOOLEANTRUE or lhs.type == TOKENS.BOOLEANFALSE) and \
            (rhs.type == TOKENS.FLOAT or rhs.type == TOKENS.BOOLEANTRUE or rhs.type == TOKENS.BOOLEANFALSE):
        result = not (isTrue(lhs)) or not (isTrue(rhs))
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # logical string
    elif (lhs.type == TOKENS.STRING or lhs.type == TOKENS.BOOLEANTRUE or lhs.type == TOKENS.BOOLEANFALSE) and \
            (rhs.type == TOKENS.STRING or rhs.type == TOKENS.BOOLEANTRUE or rhs.type == TOKENS.BOOLEANFALSE):
        result = not (isTrue(lhs)) or not (isTrue(rhs))
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))


def binaryEquality(stack):
    rhs = replaceIdentifier(stack)
    lhs = replaceIdentifier(stack)

    # Strictly String Case:
    if lhs.type == TOKENS.STRING and rhs.type == TOKENS.STRING:
        result = lhs.value == rhs.value
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Integer Case:
    elif lhs.type == TOKENS.INTEGER and rhs.type == TOKENS.INTEGER:
        result = int(lhs.value) == int(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Float Case:
    elif lhs.type == TOKENS.FLOAT and rhs.type == TOKENS.FLOAT:
        result = float(lhs.value) == float(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Logical Case:
    elif (lhs.type == TOKENS.BOOLEANTRUE or lhs.type == TOKENS.BOOLEANFALSE) and \
            (rhs.type == TOKENS.BOOLEANTRUE or rhs.type == TOKENS.BOOLEANFALSE):
        result = rhs.type == lhs.type
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Mixed Cases:
    # int float
    elif (lhs.type == TOKENS.INTEGER or lhs.type == TOKENS.FLOAT) and \
            (rhs.type == TOKENS.INTEGER or rhs.type == TOKENS.FLOAT):
        result = float(lhs.value) == float(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # int string
    elif (lhs.type == TOKENS.INTEGER or lhs.type == TOKENS.STRING) and \
            (rhs.type == TOKENS.STRING or rhs.type == TOKENS.INTEGER):
        result = str(lhs.value) == str(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # float string
    elif (lhs.type == TOKENS.FLOAT or lhs.type == TOKENS.STRING) and \
            (rhs.type == TOKENS.STRING or rhs.type == TOKENS.FLOAT):
        result = str(lhs.value) == str(lhs.value)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # logical int
    elif (lhs.type == TOKENS.INTEGER or lhs.type == TOKENS.BOOLEANTRUE or lhs.type == TOKENS.BOOLEANFALSE) and \
            (rhs.type == TOKENS.INTEGER or rhs.type == TOKENS.BOOLEANTRUE or rhs.type == TOKENS.BOOLEANFALSE):
        result = isTrue(lhs) and isTrue(rhs)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # logical float
    elif (lhs.type == TOKENS.FLOAT or lhs.type == TOKENS.BOOLEANTRUE or lhs.type == TOKENS.BOOLEANFALSE) and \
            (rhs.type == TOKENS.FLOAT or rhs.type == TOKENS.BOOLEANTRUE or rhs.type == TOKENS.BOOLEANFALSE):
        result = isTrue(lhs) and isTrue(rhs)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
        # logical string
    elif (lhs.type == TOKENS.STRING or lhs.type == TOKENS.BOOLEANTRUE or lhs.type == TOKENS.BOOLEANFALSE) and \
            (rhs.type == TOKENS.STRING or rhs.type == TOKENS.BOOLEANTRUE or rhs.type == TOKENS.BOOLEANFALSE):
        result = isTrue(lhs) and isTrue(rhs)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
