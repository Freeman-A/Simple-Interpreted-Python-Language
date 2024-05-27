# sipl_parser.py
from tokenizer import TOKENS


def siplParser(tokens):
    """Parse tokens into Reverse Polish Notation (RPN) using the Shunting Yard algorithm."""
    stack = []
    rpn = []

    # Handle operator precedence here using a dictionary rather than assigning precedence in the Token class
    precedence = {
        TOKENS.BADD: 4,        # Addition
        TOKENS.BSUB: 4,        # Subtraction
        TOKENS.BMULT: 5,       # Multiplication
        TOKENS.BDIV: 5,        # Division
        TOKENS.NEGINTEGER: 6,  # Unary negation
        TOKENS.LPAREN: 0,      # Left parenthesis (lowest precedence)
        TOKENS.RPAREN: 0,      # Right parenthesis (lowest precedence)
        TOKENS.NOTEQUAL: 3,    # Not equal
        TOKENS.EQUALITY: 3,    # Equality
        TOKENS.AND: 2,         # Logical AND
        TOKENS.OR: 1,          # Logical OR
        TOKENS.NOT: 6,         # Logical NOT (unary)
        TOKENS.GREATER: 3,     # Greater than
        TOKENS.LESS: 3         # Less than
    }

    for token in tokens:
        if token.superType == TOKENS.VALUE:
            rpn.append(token)  # Directly add values to the RPN output
        elif token.type == TOKENS.LPAREN:
            stack.append(token)  # Push left parenthesis to the stack
        elif token.type == TOKENS.RPAREN:
            # Pop from stack to RPN until a left parenthesis is encountered
            while stack and stack[-1].type != TOKENS.LPAREN:
                rpn.append(stack.pop())
            if stack:
                stack.pop()  # Pop the left parenthesis from the stack
            else:
                raise ValueError("Mismatched parentheses detected")
        elif token.superType == TOKENS.OPERATOR:
            # Pop from stack to RPN based on precedence
            while stack and precedence.get(stack[-1].type, 0) >= precedence[token.type]:
                rpn.append(stack.pop())
            stack.append(token)
        elif token.type == TOKENS.TERMINATOR:
            # Pop everything from stack to RPN until the stack is empty
            while stack:
                rpn.append(stack.pop())
            rpn.append(token)

    # Pop any remaining operators from the stack to the RPN output
    while stack:
        rpn.append(stack.pop())

    return rpn
