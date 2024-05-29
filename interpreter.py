# interpreter.py
import operators
from tokenizer import TOKENS


def evaluator(rpn):
    """Evaluate a list of tokens in Reverse Polish Notation (RPN)."""
    stack = []
    results = []

    for token in rpn:
        if token.superType == TOKENS.VALUE:
            # Push value tokens onto the stack
            stack.append(token)
        elif token.superType == TOKENS.OPERATOR:
            # Handle binary and unary operations based on token type
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
            elif token.type == TOKENS.AND: 
                operators.binaryAND(stack)
            elif token.type == TOKENS.OR: 
                operators.binaryOR(stack)
            elif token.type == TOKENS.GREATER:
                operators.binaryGreater(stack)
            elif token.type == TOKENS.LESS:
            
                operators.binaryLess(stack)
        elif token.type == TOKENS.TERMINATOR:
            # Handle terminator tokens, pop the stack and process result
            if stack:
                result_token = stack.pop()
                if result_token.type == TOKENS.STRING and result_token.value == 'Error':
                    # Append error message if result indicates an error
                    results.append('Error1')
                else:
                    # Append the value of the result token
                    results.append(result_token.value)
            else:
                # Append error message if stack is empty
                results.append('Error2')

    # Return results if available, otherwise return generic error message
    return results if results else ['Error']
