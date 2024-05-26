# interpreter.py
import operators
from tokenizer import TOKENS


def evaluator(rpn):
    """Evaluate a list of tokens in Reverse Polish Notation (RPN)."""
    stack = []
    results = []

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
            elif token.type == TOKENS.EQUALITY:
                operators.binaryEquality(stack)
            elif token.type == TOKENS.NOTEQUAL:
                operators.binaryNotEqual(stack)
        elif token.type == TOKENS.TERMINATOR:
            if stack:
                result_token = stack.pop()
                if result_token.type == TOKENS.STRING and result_token.value == 'Error':
                    results.append('Error1')
                else:
                    results.append(result_token.value)
            else:
                results.append('Error2')

    return results if results else ['Error']
