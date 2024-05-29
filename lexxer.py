# lexxer.py
from tokenizer import TOKENS, Token


def lexxer(line):
    """Lexical analyzer to tokenize the input string."""
    tokens = []
    position = 0

    while position < len(line):
        character = line[position]

        # Handle statement terminators
        if character == ';':
            tokens.append(
                Token(TOKENS.TERMINATOR, character, TOKENS.TERMINATOR))
            position += 1

        # Handle numbers (integers and floats)
        elif character.isdigit() or (character == '.' and position + 1 < len(line) and line[position + 1].isdigit()):
            start = position
            while position < len(line) and (line[position].isdigit() or line[position] == '.'):
                position += 1
            token_value = line[start:position]
            if '.' in token_value:
                tokens.append(Token(TOKENS.FLOAT, token_value, TOKENS.VALUE))
            else:
                tokens.append(Token(TOKENS.INTEGER, token_value, TOKENS.VALUE))

        # Handle identifiers and keywords
        elif character.isalpha():

            start = position
            while position < len(line) and line[position].isalnum():
                position += 1
            token = line[start:position]

            if token.lower() == 'false':
                tokens.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))

            elif token.lower() == 'true':
                tokens.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))

            elif token.lower() == 'and': 
                tokens.append(Token(TOKENS.AND, 'and', TOKENS.OPERATOR))
            
            elif token.lower() == 'or':
                tokens.append(Token(TOKENS.OR, 'or', TOKENS.OPERATOR))

            elif token.upper() in TOKENS.__dict__.keys():
                    
                    Token(TOKENS.IDENTIFIER, token, TOKENS.IDENTIFIER)

        # Handle string literals
        elif character == '\"':
            start = position
            end = position + 1
            while end < len(line) and line[end] != '\"':
                end += 1
            if end >= len(line):
                raise ValueError("Unterminated string literal")
            end += 1
            token = line[start + 1:end - 1]
            tokens.append(Token(TOKENS.STRING, token, TOKENS.VALUE))
            position = end

        # Handle parentheses
        elif character == '(':
            tokens.append(Token(TOKENS.LPAREN, '(', TOKENS.SEPARATOR))
            position += 1

        elif character == ')':
            tokens.append(Token(TOKENS.RPAREN, ')', TOKENS.SEPARATOR))
            position += 1

        # Handle operators
        elif character == '+' or character == '–':
            # Treat en dash '–' as minus '-'
            character = '-' if character == '–' else character
            tokens.append(Token(TOKENS.BADD if character ==
                          '+' else TOKENS.BSUB, character, TOKENS.OPERATOR))
            position += 1

        elif character == '-':
            if position == 0 or tokens[-1].superType in [TOKENS.OPERATOR, TOKENS.LPAREN]:
                tokens.append(Token(TOKENS.NEGINTEGER, "-", TOKENS.OPERATOR))
            else:
                tokens.append(Token(TOKENS.BSUB, "-", TOKENS.OPERATOR))
            position += 1

        elif character == '*':
            tokens.append(Token(TOKENS.BMULT, '*', TOKENS.OPERATOR))
            position += 1

        elif character == '/':
            tokens.append(Token(TOKENS.BDIV, '/', TOKENS.OPERATOR))
            position += 1

        elif character == '&':
            tokens.append(Token(TOKENS.AND, '&', TOKENS.OPERATOR))
            position += 1

        elif character == '|':
            tokens.append(Token(TOKENS.OR, '|', TOKENS.OPERATOR))
            position += 1

        elif character == '~':
            tokens.append(Token(TOKENS.NOT, '~', TOKENS.OPERATOR))
            position += 1

        # Handle assignment and equality
        elif character == '=':
            start = position
            if position + 1 < len(line) and line[position + 1] == '=':
                tokens.append(Token(TOKENS.EQUALITY, '==', TOKENS.OPERATOR))
                position += 2
            else:
                tokens.append(Token(TOKENS.ASSIGNMENT, '=', TOKENS.OPERATOR))
                position += 1

        # Handle relational operators
        elif character == '<':
            if position + 1 < len(line) and line[position + 1] == '=':
                tokens.append(Token(TOKENS.LESSEQUAL, '<=', TOKENS.OPERATOR))
                position += 2
            else:
                tokens.append(Token(TOKENS.LESS, '<', TOKENS.OPERATOR))
                position += 1

        elif character == '>':
            if position + 1 < len(line) and line[position + 1] == '=':
                tokens.append(
                    Token(TOKENS.GREATEREQUAL, '>=', TOKENS.OPERATOR))
                position += 2
            else:
                tokens.append(Token(TOKENS.GREATER, '>', TOKENS.OPERATOR))
                position += 1

        # Handle not equal '!='
        elif character == '!':
            if position + 1 < len(line) and line[position + 1] == '=':
                tokens.append(Token(TOKENS.NOTEQUAL, '!=', TOKENS.OPERATOR))
                position += 2
            else:
                tokens.append(Token(TOKENS.NOT, '!', TOKENS.OPERATOR))
                position += 1
        else:
            position += 1

    return tokens