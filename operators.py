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
                     True, TOKENS.VALUE))
    else:
        stack.append(Token(TOKENS.BOOLEANFALSE,
                     False, TOKENS.VALUE))


def binaryOR(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    logicalLeft = isTrue(left)
    logicalRight = isTrue(right)

    result = logicalLeft or logicalRight
    if result:
        stack.append(Token(TOKENS.BOOLEANTRUE,
                     True, TOKENS.VALUE))
    else:
        stack.append(Token(TOKENS.BOOLEANFALSE,
                     False, TOKENS.VALUE))


def binaryNotEqual(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    # Strictly String Case:
    if left.type == TOKENS.STRING and right.type == TOKENS.STRING:
        result = left.value != right.value
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Integer Case:
    elif left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) != int(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Float Case:
    elif left.type == TOKENS.FLOAT and right.type == TOKENS.FLOAT:
        result = float(left.value) != float(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Logical Case:
    elif (left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
            (right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
        result = right.type != left.type
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Mixed Cases:
    # int float
    elif (left.type == TOKENS.INTEGER or left.type == TOKENS.FLOAT) and \
            (right.type == TOKENS.INTEGER or right.type == TOKENS.FLOAT):
        result = float(left.value) != float(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # int string
    elif (left.type == TOKENS.INTEGER or left.type == TOKENS.STRING) and \
            (right.type == TOKENS.STRING or right.type == TOKENS.INTEGER):
        result = str(left.value) != str(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # float string
    elif (left.type == TOKENS.FLOAT or left.type == TOKENS.STRING) and \
            (right.type == TOKENS.STRING or right.type == TOKENS.FLOAT):
        result = str(left.value) != str(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # logical int
    elif (left.type == TOKENS.INTEGER or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
            (right.type == TOKENS.INTEGER or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
        result = not (isTrue(left)) or not (isTrue(right))
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # logical float
    elif (left.type == TOKENS.FLOAT or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
            (right.type == TOKENS.FLOAT or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
        result = not (isTrue(left)) or not (isTrue(right))
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # logical string
    elif (left.type == TOKENS.STRING or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
            (right.type == TOKENS.STRING or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
        result = not (isTrue(left)) or not (isTrue(right))
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))


def binaryEquality(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    # Strictly String Case:
    if left.type == TOKENS.STRING and right.type == TOKENS.STRING:
        result = left.value == right.value
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Integer Case:
    elif left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) == int(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Float Case:
    elif left.type == TOKENS.FLOAT and right.type == TOKENS.FLOAT:
        result = float(left.value) == float(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Strictly Logical Case:
    elif (left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
            (right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
        result = right.type == left.type
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # Mixed Cases:
    # int float
    elif (left.type == TOKENS.INTEGER or left.type == TOKENS.FLOAT) and \
            (right.type == TOKENS.INTEGER or right.type == TOKENS.FLOAT):
        result = float(left.value) == float(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # int string
    elif (left.type == TOKENS.INTEGER or left.type == TOKENS.STRING) and \
            (right.type == TOKENS.STRING or right.type == TOKENS.INTEGER):
        result = str(left.value) == str(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # float string
    elif (left.type == TOKENS.FLOAT or left.type == TOKENS.STRING) and \
            (right.type == TOKENS.STRING or right.type == TOKENS.FLOAT):
        result = str(left.value) == str(right.value)  # corrected
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # logical int
    elif (left.type == TOKENS.INTEGER or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
            (right.type == TOKENS.INTEGER or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
        result = isTrue(left) and isTrue(right)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # logical float
    elif (left.type == TOKENS.FLOAT or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
            (right.type == TOKENS.FLOAT or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
        result = isTrue(left) and isTrue(right)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
    # logical string
    elif (left.type == TOKENS.STRING or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
            (right.type == TOKENS.STRING or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
        result = isTrue(left) and isTrue(right)
        if result:
            stack.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))


def binaryGreater(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)
    if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) > int(right.value)
    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) > float(right.value)
    else:
        result = False
    stack.append(Token(TOKENS.BOOLEANTRUE if result else TOKENS.BOOLEANFALSE,
                 True if result else False, TOKENS.VALUE))


def binaryLess(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)
    if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) < int(right.value)
    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) < float(right.value)
    else:
        result = False
    stack.append(Token(TOKENS.BOOLEANTRUE if result else TOKENS.BOOLEANFALSE,
                 True if result else False, TOKENS.VALUE))
