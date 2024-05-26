# lexxer.py
from tokenizer import TOKENS, Token


def lexxer(line):
    """Lexical analyzer to tokenize the input string."""
    tokens = []
    position = 0

    while position < len(line):
        character = line[position]

        if character == ';':
            tokens.append(
                Token(TOKENS.TERMINATOR, character, TOKENS.TERMINATOR))
            position += 1

        elif character.isdigit() or (character == '.' and position + 1 < len(line) and line[position + 1].isdigit()):
            start = position
            while position < len(line) and (line[position].isdigit() or line[position] == '.'):
                position += 1
            token_value = line[start:position]
            if '.' in token_value:
                tokens.append(Token(TOKENS.FLOAT, token_value, TOKENS.VALUE))
            else:
                tokens.append(Token(TOKENS.INTEGER, token_value, TOKENS.VALUE))

        elif character.isalpha():
            start = position
            while position < len(line) and line[position].isalnum():
                position += 1
            token = line[start:position]

            if token == 'false' or token == 'False':
                tokens.append(Token(TOKENS.BOOLEANFALSE, False, TOKENS.VALUE))
            elif token == 'true' or token == 'True':
                tokens.append(Token(TOKENS.BOOLEANTRUE, True, TOKENS.VALUE))

            elif token in TOKENS.__dict__.values():
                tokens.append(Token(token, token))
                if token == 'if':
                    tokens.append(Token(TOKENS.IF, token, TOKENS.KEYWORD))
                elif token == 'else':
                    tokens.append(Token(TOKENS.ELSE, token, TOKENS.KEYWORD))
                elif token == 'while':
                    tokens.append(Token(TOKENS.WHILE, token, TOKENS.KEYWORD))
                elif token == 'endif':
                    tokens.append(Token(TOKENS.ENDIF, token, TOKENS.KEYWORD))
                elif token == 'var':
                    tokens.append(Token(TOKENS.VAR, token, TOKENS.KEYWORD))
            else:
                tokens.append(
                    Token(TOKENS.IDENTIFIER, token, TOKENS.IDENTIFIER))

        elif character == '\"':
            start = position
            end = position + 1
            while end < len(line) and line[end] != '\"':
                end += 1
            if end >= len(line):
                break
            end += 1
            token = line[start + 1:end - 1]
            tokens.append(Token(TOKENS.STRING, token, TOKENS.VALUE))
            position = end

        elif character == '(':
            tokens.append(Token(TOKENS.LPAREN, '(', TOKENS.SEPARATOR))
            position += 1

        elif character == ')':
            tokens.append(Token(TOKENS.RPAREN, ')', TOKENS.SEPARATOR))
            position += 1

        elif character == '+':
            tokens.append(Token(TOKENS.BADD, '+', TOKENS.OPERATOR))
            position += 1

        elif character == '-':
            if position == 0 or tokens[-1].superType == TOKENS.OPERATOR:
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

        elif character == "&":
            tokens.append(Token(TOKENS.AND, '&', TOKENS.OPERATOR))
            position += 1

        elif character == "|":
            tokens.append(Token(TOKENS.OR, '|', TOKENS.OPERATOR))
            position += 1

        elif character == '~':
            tokens.append(Token(TOKENS.NOT, '~', TOKENS.OPERATOR))
            position += 1

        elif character == '=':
            start = position
            while position < len(line) and line[position] == '=':
                position += 1
            token = line[start:position]

            if token == '=':
                tokens.append(Token(TOKENS.ASSIGNMENT, token, TOKENS.OPERATOR))
            elif token == '==':
                tokens.append(Token(TOKENS.EQUALITY, token, TOKENS.OPERATOR))

        elif character == ':':
            start = position
            end = position
            while end < len(line) and line[end] == '=':
                end += 1
            token = line[start:end]

            if token == ':=':
                tokens.append(Token(TOKENS.WALRUS, ':=', TOKENS.OPERATOR))
                position = end
            else:
                position += 1

        elif character == '<':
            start = position
            end = position + 1

            if end < len(line) and line[end] == '=':
                tokens.append(Token(TOKENS.LESSEQUAL, '<=', TOKENS.OPERATOR))
                position += 2
            else:
                tokens.append(Token(TOKENS.LESS, '<', TOKENS.OPERATOR))
                position += 1

        elif character == '>':
            start = position
            end = position + 1

            if end < len(line) and line[end] == '=':
                tokens.append(
                    Token(TOKENS.GREATEREQUAL, '>=', TOKENS.OPERATOR))
                position += 2
            else:
                tokens.append(Token(TOKENS.GREATER, '>', TOKENS.OPERATOR))
                position += 1

        elif character == '!':
            start = position
            end = position + 1

            if end < len(line) and line[end] == '=':
                tokens.append(Token(TOKENS.NOTEQUAL, '!=', TOKENS.OPERATOR))
                position += 2
            else:
                tokens.append(Token(TOKENS.NOT, '!', TOKENS.OPERATOR))
                position += 1
        else:
            position += 1

    return tokens
