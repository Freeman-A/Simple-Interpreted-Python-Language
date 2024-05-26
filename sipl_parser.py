from tokenizer import TOKENS, Token
from lexxer import lexxer
import variable
import operators


from tokenizer import TOKENS, Token
from lexxer import lexxer
import variable
import operators


def siplParser(tokens):
    stack = []
    rpn = []

    precedence = {
        TOKENS.BADD: 1,
        TOKENS.BSUB: 1,
        TOKENS.BMULT: 2,
        TOKENS.BDIV: 2,
        TOKENS.NEGINTEGER: 3,  # High precedence for unary negation
        TOKENS.LPAREN: 0,
        TOKENS.RPAREN: 0,
    }

    for token in tokens:
        if token.superType == TOKENS.VALUE:
            rpn.append(token)
        elif token.type == TOKENS.LPAREN:
            stack.append(token)
        elif token.type == TOKENS.RPAREN:
            while stack and stack[-1].type != TOKENS.LPAREN:
                rpn.append(stack.pop())
            stack.pop()  # pop the left parenthesis
        elif token.superType == TOKENS.OPERATOR:
            while stack and precedence.get(stack[-1].type, 0) >= precedence[token.type]:
                rpn.append(stack.pop())
            stack.append(token)
        elif token.type == TOKENS.TERMINATOR:
            while stack:
                rpn.append(stack.pop())
            rpn.append(token)

    while stack:
        rpn.append(stack.pop())

    return rpn
