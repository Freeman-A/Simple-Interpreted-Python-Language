from tokenizer import TOKENS, Token
from lexxer import lexxer
import variable
import operators


def siplParser(tokens):
    stack = []
    rpn = []

    if tokens[0].superType == TOKENS.KEYWORD:
        pass

    else:
        for token in tokens:
            if token.superType == TOKENS.VALUE:
                rpn.append(token)
            elif token.superType == TOKENS.IDENTIFIER:
                stack.append(token)
            elif token.superType == TOKENS.SEPARATOR:
                if len(stack) > 0:
                    topOperator = stack[-1]
                    if topOperator.type == TOKENS.LPAREN:
                        rpn.append(stack.pop())
                    stack.append(token)
                else:
                    stack.append(token)
            elif token.type == TOKENS.LPAREN:
                stack.append(token)
            elif token.type == TOKENS.RPAREN:
                while len(stack) > 0:
                    topOperator = stack.pop()
                    if topOperator.type == TOKENS.LPAREN:
                        break
                    rpn.append(topOperator)
            elif token.type == TOKENS.TERMINATOR:
                while len(stack) > 0:
                    rpn.append(stack.pop())
                rpn.append(token)

        while len(stack) > 0:
            rpn.append(stack.pop())
    return rpn
