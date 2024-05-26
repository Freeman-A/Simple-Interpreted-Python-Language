import operators
from tokenizer import TOKENS, Token


def evaluator(rpn):
    stack = []

    for token in rpn:
        if token.superType == TOKENS.VALUE:
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
            elif token.type == TOKENS.NEGINTEGER:
                operators.unaryNegation(stack)
        elif token.type == TOKENS.TERMINATOR:
            if stack:
                result_token = stack.pop()
                if result_token.type == TOKENS.STRING and result_token.value == 'Error':
                    return 'Error'
                else:
                    return result_token.value

    return 'Error'  # Return 'Error' if stack is empty or invalid