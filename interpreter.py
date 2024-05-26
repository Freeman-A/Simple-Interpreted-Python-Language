import operators
from tokenizer import TOKENS, Token


def evaluator(rpn):
    result = None
    stack = []
    type = None

    for token in rpn:
        if token.superType == TOKENS.VALUE:

            if token.type == TOKENS.NUMBER:
                if operators.isInt(token.value):
                    token.type = TOKENS.INTEGER
                elif operators.isFloat(token.value):
                    token.type = TOKENS.FLOAT

            elif token.type == TOKENS.BOLEANTRUE or token.type == TOKENS.BOLEANFALSE:
                pass

            else:
                print(token)
                token.type = TOKENS.STRING

            stack.append(token)

        elif token.superType == TOKENS.IDENTIFIER:
            stack.append(token)
        elif token.superType == TOKENS.OPERATOR:
            if token.type == TOKENS.BADD:
                operators.binaryAdd(stack)
            elif token.type == TOKENS.BSUB:
                operators.binarySubtraction(stack)
            elif token.type == TOKENS.BMULT:
                operators.binaryMultiply(stack)
            elif token.type == TOKENS.BDIV:
                operators.binaryDivision(stack)
            elif token.type == TOKENS.AND:
                operators.binaryAnd(stack)
            elif token.type == TOKENS.OR:
                operators.binaryOr(stack)
            elif token.type == TOKENS.NOT:
                operators.binaryNot(stack)
            elif token.type == TOKENS.EQUALITY:
                operators.binaryEquality(stack)
            elif token.type == TOKENS.ASSIGNMENT:
                operators.binaryAssignment(stack)
            elif token.type == TOKENS.NEGINTEGER:
                operators.unaryNegation(stack)
        else:
            pass
    return result
