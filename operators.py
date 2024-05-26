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
    elif token.type == TOKENS.BOLEANTRUE:
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

    elif right.type == TOKENS.BOLEANTRUE:
        var.type = TOKENS.BOLEANTRUE
        var.strValue = int(right.value)

    elif right.type == TOKENS.BOLEANFALSE:
        var.type = TOKENS.BOLEANFALSE
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
        stack.append(Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
    else:
        stack.append(Token(TOKENS.BOLEANFALSE,
                     TOKENS.BOLEANFALSE, TOKENS.VALUE))


def binaryOR(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    logicalLeft = isTrue(left)
    logicalRight = isTrue(right)

    result = logicalLeft or logicalRight
    if result:
        stack.append(Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
    else:
        stack.append(Token(TOKENS.BOLEANFALSE,
                     TOKENS.BOLEANFALSE, TOKENS.VALUE))


def binaryNotEqual(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    if left.type == TOKENS.STRING and right.type == TOKENS.STRING:
        result = left.value != right.value
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) != int(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) != float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.BOLEANTRUE or right.type == TOKENS.BOLEANFALSE:
        result = right.type != left.type
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.INTEGER and right.type == TOKENS.FLOAT:
        result = float(left.value) != float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT and right.type == TOKENS.INTEGER:
        result = float(left.value) != float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.INTEGER and right.type == TOKENS.STRING:
        result = int(left.value) != int(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.STRING and right.type == TOKENS.INTEGER:
        result = int(left.value) != int(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT and right.type == TOKENS.STRING:
        result = float(left.value) != float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.STRING and right.type == TOKENS.FLOAT:
        result = float(left.value) != float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.INTEGER or left.type == TOKENS.BOLEANTRUE:
        result = int(left.value) != int(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT or left.type == TOKENS.BOLEANTRUE:
        result = float(left.value) != float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.STRING or left.type == TOKENS.BOLEANTRUE:
        result = left.value != right.value
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))


def binaryEquality(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    if left.type == TOKENS.STRING and right.type == TOKENS.STRING:
        result = left.value == right.value
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) == int(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) == float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.BOLEANTRUE or right.type == TOKENS.BOLEANFALSE:
        result = right.type == left.type
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.INTEGER and right.type == TOKENS.FLOAT:
        result = float(left.value) == float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT and right.type == TOKENS.INTEGER:
        result = float(left.value) == float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.INTEGER and right.type == TOKENS.STRING:
        result = int(left.value) == int(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.STRING and right.type == TOKENS.INTEGER:
        result = int(left.value) == int(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT and right.type == TOKENS.STRING:
        result = float(left.value) == float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.STRING and right.type == TOKENS.FLOAT:
        result = float(left.value) == float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.INTEGER or left.type == TOKENS.BOLEANTRUE:
        result = int(left.value) == int(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT or left.type == TOKENS.BOLEANTRUE:
        result = float(left.value) == float(right.value)
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))

    elif left.type == TOKENS.STRING or left.type == TOKENS.BOLEANTRUE:
        result = left.value == right.value
        if result:
            stack.append(
                Token(TOKENS.BOLEANTRUE, TOKENS.BOLEANTRUE, TOKENS.VALUE))
        else:
            stack.append(Token(TOKENS.BOLEANFALSE,
                         TOKENS.BOLEANFALSE, TOKENS.VALUE))
