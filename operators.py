import variable
from tokenizer import TOKENS, Token

# Helper function to check if a string can be converted to a float


def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Helper function to check if a string can be converted to an integer


def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# Function to determine the truthiness of a token based on its type and value


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

# Function to replace an identifier token with its value from global variables


def replaceIdentifier(stack):
    if not stack:
        raise ValueError("Stack is empty. Cannot pop value.")

    value = stack.pop()
    if value.type == TOKENS.IDENTIFIER:
        if value.value in variable.globalVariables:
            temp = variable.globalVariables[value.value]
            value.value = temp.strValue
            value.type = temp.type
            value.superType = TOKENS.VALUE
        else:
            raise ValueError(
                f"Identifier {value.value} not found in global variables.")

    return value

# Function to handle binary addition for different token types


def binaryAdd(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) + int(right.value)
        stack.append(Token(TOKENS.INTEGER, str(result), TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) + float(right.value)
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))

    elif left.type == TOKENS.STRING and right.type == TOKENS.STRING:
        result = left.value + right.value
        stack.append(Token(TOKENS.STRING, result, TOKENS.VALUE))

    else:
        result = str(left.value) + str(right.value)
        stack.append(Token(TOKENS.STRING, result, TOKENS.VALUE))

# Function to handle variable assignment


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

# Function to handle unary negation for integers and floats


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

# Function to handle binary subtraction for different token types


def binarySubtraction(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) - int(right.value)
        stack.append(Token(TOKENS.INTEGER, str(result), TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) - float(right.value)
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))

    else:
        result = 'Error'
        stack.append(Token(TOKENS.STRING, result, TOKENS.VALUE))

# Function to handle binary multiplication for different token types


def binaryMultiply(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
        result = int(left.value) * int(right.value)
        stack.append(Token(TOKENS.INTEGER, str(result), TOKENS.VALUE))

    elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
        result = float(left.value) * float(right.value)
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))

    else:
        result = 'Error'
        stack.append(Token(TOKENS.STRING, result, TOKENS.VALUE))

# Function to handle binary division for different token types


def binaryDivision(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    try:
        if (right.type == TOKENS.INTEGER and int(right.value) == 0) or (right.type == TOKENS.FLOAT and float(right.value) == 0.0):
            raise ZeroDivisionError("Division by zero.")

        left_value = float(left.value) if left.type in [
            TOKENS.INTEGER, TOKENS.FLOAT] else 0.0
        right_value = float(right.value) if right.type in [
            TOKENS.INTEGER, TOKENS.FLOAT] else 0.0

        result = left_value / right_value
        stack.append(Token(TOKENS.FLOAT, str(result), TOKENS.VALUE))

    except ZeroDivisionError as e:
        stack.append(Token(TOKENS.STRING, str(e), TOKENS.VALUE))

# Function to handle logical AND operation


def binaryAND(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    logicalLeft = isTrue(left)
    logicalRight = isTrue(right)

    result = logicalLeft and logicalRight
    stack.append(Token(
        TOKENS.BOOLEANTRUE if result else TOKENS.BOOLEANFALSE, result, TOKENS.VALUE))

# Function to handle logical OR operation


def binaryOR(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    logicalLeft = isTrue(left)
    logicalRight = isTrue(right)

    result = logicalLeft or logicalRight
    stack.append(Token(
        TOKENS.BOOLEANTRUE if result else TOKENS.BOOLEANFALSE, result, TOKENS.VALUE))

# Function to handle inequality comparison


def binaryNotEqual(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    try:
        if left.type == TOKENS.STRING and right.type == TOKENS.STRING:
            result = left.value != right.value
        elif left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
            result = int(left.value) != int(right.value)
        elif left.type == TOKENS.FLOAT and right.type == TOKENS.FLOAT:
            result = float(left.value) != float(right.value)
        elif (left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
             (right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
            result = right.type != left.type
        elif (left.type == TOKENS.INTEGER or left.type == TOKENS.FLOAT) and \
             (right.type == TOKENS.INTEGER or right.type == TOKENS.FLOAT):
            result = float(left.value) != float(right.value)
        elif (left.type == TOKENS.INTEGER or left.type == TOKENS.STRING) and \
             (right.type == TOKENS.STRING or right.type == TOKENS.INTEGER):
            result = str(left.value) != str(right.value)
        elif (left.type == TOKENS.FLOAT or left.type == TOKENS.STRING) and \
             (right.type == TOKENS.STRING or right.type == TOKENS.FLOAT):
            result = str(left.value) != str(right.value)
        elif (left.type == TOKENS.INTEGER or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
             (right.type == TOKENS.INTEGER or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
            result = not (isTrue(left)) or not (isTrue(right))
        elif (left.type == TOKENS.FLOAT or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
             (right.type == TOKENS.FLOAT or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
            result = not (isTrue(left)) or not (isTrue(right))
        elif (left.type == TOKENS.STRING or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
             (right.type == TOKENS.STRING or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
            result = not (isTrue(left)) or not (isTrue(right))
        else:
            result = True

        stack.append(Token(
            TOKENS.BOOLEANTRUE if result else TOKENS.BOOLEANFALSE, result, TOKENS.VALUE))
    except Exception as e:
        stack.append(Token(TOKENS.STRING, str(e), TOKENS.VALUE))

# Function to handle equality comparison


def binaryEquality(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    try:
        if left.type == TOKENS.STRING and right.type == TOKENS.STRING:
            result = left.value == right.value
        elif left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
            result = int(left.value) == int(right.value)
        elif left.type == TOKENS.FLOAT and right.type == TOKENS.FLOAT:
            result = float(left.value) == float(right.value)
        elif (left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
             (right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
            result = right.type == left.type
        elif (left.type == TOKENS.INTEGER or left.type == TOKENS.FLOAT) and \
             (right.type == TOKENS.INTEGER or right.type == TOKENS.FLOAT):
            result = float(left.value) == float(right.value)
        elif (left.type == TOKENS.INTEGER or left.type == TOKENS.STRING) and \
             (right.type == TOKENS.STRING or right.type == TOKENS.INTEGER):
            result = str(left.value) == str(right.value)
        elif (left.type == TOKENS.FLOAT or left.type == TOKENS.STRING) and \
             (right.type == TOKENS.STRING or right.type == TOKENS.FLOAT):
            result = str(left.value) == str(right.value)
        elif (left.type == TOKENS.INTEGER or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
             (right.type == TOKENS.INTEGER or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
            result = isTrue(left) and isTrue(right)
        elif (left.type == TOKENS.FLOAT or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
             (right.type == TOKENS.FLOAT or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
            result = isTrue(left) and isTrue(right)
        elif (left.type == TOKENS.STRING or left.type == TOKENS.BOOLEANTRUE or left.type == TOKENS.BOOLEANFALSE) and \
             (right.type == TOKENS.STRING or right.type == TOKENS.BOOLEANTRUE or right.type == TOKENS.BOOLEANFALSE):
            result = isTrue(left) and isTrue(right)
        else:
            result = False

        stack.append(Token(
            TOKENS.BOOLEANTRUE if result else TOKENS.BOOLEANFALSE, result, TOKENS.VALUE))
    except Exception as e:
        stack.append(Token(TOKENS.STRING, str(e), TOKENS.VALUE))

# Function to handle greater than comparison


def binaryGreater(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    try:
        if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
            result = int(left.value) > int(right.value)
        elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
            result = float(left.value) > float(right.value)
        else:
            result = False

        stack.append(Token(
            TOKENS.BOOLEANTRUE if result else TOKENS.BOOLEANFALSE, result, TOKENS.VALUE))
    except Exception as e:
        stack.append(Token(TOKENS.STRING, str(e), TOKENS.VALUE))

# Function to handle less than comparison


def binaryLess(stack):
    right = replaceIdentifier(stack)
    left = replaceIdentifier(stack)

    try:
        if left.type == TOKENS.INTEGER and right.type == TOKENS.INTEGER:
            result = int(left.value) < int(right.value)
        elif left.type == TOKENS.FLOAT or right.type == TOKENS.FLOAT:
            result = float(left.value) < float(right.value)
        else:
            result = False

        stack.append(Token(
            TOKENS.BOOLEANTRUE if result else TOKENS.BOOLEANFALSE, result, TOKENS.VALUE))
    except Exception as e:
        stack.append(Token(TOKENS.STRING, str(e), TOKENS.VALUE))
