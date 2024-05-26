# sipl_parser.py
from tokenizer import TOKENS


def siplParser(tokens):
    """Parse tokens into Reverse Polish Notation (RPN) using the Shunting Yard algorithm."""
    stack = []
    rpn = []

    # Handle operator precedence here using a dictionary rather than assinging precedence in the Token class
    precedence = {
        TOKENS.BADD: 2,
        TOKENS.BSUB: 1,
        TOKENS.BMULT: 3,
        TOKENS.BDIV: 3,
        TOKENS.NEGINTEGER: 4,
        TOKENS.LPAREN: 0,
        TOKENS.RPAREN: 0,
        TOKENS.NOTEQUAL: 1,
        TOKENS.EQUALITY: 2,
        TOKENS.AND: 1,
        TOKENS.OR: 1,
        TOKENS.NOT: 4,
        TOKENS.GREATER: 1,
        TOKENS.LESS: 1
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
