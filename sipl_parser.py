from tokenizer import TOKENS, Token
from lexxer import lexxer
import variable
import operators


def siplParser(tokens):
    stack = []
    rpn = []

    for token in tokens:

        if token.superType == TOKENS.VALUE:
            rpn.append(token)
        elif token.superType == TOKENS.IDENTIFIER:
            stack.append(token)
        elif token.superType == TOKENS.SEPARATOR:
            if stack:
                topOperator = stack[-1]
                if topOperator.type == TOKENS.LPAREN:
                    rpn.append(stack.pop())

                stack.append(token)

            else:
                stack.append(token)
        elif token.type == TOKENS.LPAREN:
            stack.append(token)
        elif token.type == TOKENS.RPAREN:
            while stack:
                topOperator = stack.pop()
                if topOperator.type == TOKENS.LPAREN:
                    break
                rpn.append(topOperator)
        elif token.type == TOKENS.TERMINATOR:
            while stack:
                rpn.append(stack.pop())

            rpn.append(token)

        else:
            while stack and (stack[-1].superType == TOKENS.OPERATOR or stack[-1].type == TOKENS.OPERATOR):
                rpn.append(stack.pop())

            stack.append(token)

    while stack:
        rpn.append(stack.pop())

    return rpn
