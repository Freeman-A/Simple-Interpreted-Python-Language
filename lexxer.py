from tokenizer import TOKENS, Token


def lexxer(line):
    tokens = []
    position = 0

    while position < len(line):
        character = line[position]

        if character == ';':
            tokens.append(
                Token(TOKENS.TERMINATOR, character, TOKENS.TERMINATOR))
            position += 1

        elif character.isdigit():
            start = position
            while position < len(line) and (line[position].isdigit() or line[position] == '.'):
                position += 1
            value = line[start:position]
            if '.' in value:
                tokens.append(Token(TOKENS.FLOAT, value, TOKENS.VALUE))
            else:
                tokens.append(Token(TOKENS.INTEGER, value, TOKENS.VALUE))

        elif character.isalpha() or character == '_':
            start = position
            while position < len(line) and (line[position].isalnum() or line[position] == '_'):
                position += 1
            token = line[start:position]

            if token in ['false', 'False']:
                tokens.append(Token(TOKENS.KEYWORD, False, TOKENS.VALUE))

            elif token in ['true', 'True']:
                tokens.append(Token(TOKENS.KEYWORD, True, TOKENS.VALUE))

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
            position += 1
            while position < len(line) and line[position] != '\"':
                position += 1
            tokens.append(
                Token(TOKENS.STRING, line[start + 1:position], TOKENS.VALUE))
            position += 1

        elif character == '(':
            tokens.append(Token(TOKENS.LPAREN, '(', TOKENS.SEPARATOR))
            position += 1

        elif character == ')':
            tokens.append(Token(TOKENS.RPAREN, ')', TOKENS.SEPARATOR))
            position += 1

        elif character == '+':
            tokens.append(Token(TOKENS.BADD, '+', TOKENS.OPERATOR))
            position += 1
        elif character == "-":
            if position == 0:
                tokens.append(Token(TOKENS.NEGINTEGER, "-", TOKENS.OPERATOR))
            elif tokens[-1].superType == TOKENS.OPERATOR:
                tokens.append(Token(TOKENS.NEGINTEGER, "-", TOKENS.OPERATOR))
            else:
                tokens.append(Token(TOKENS.BINARYSUB, "-", TOKENS.OPERATOR))
            position += 1

        elif character == '*':
            tokens.append(Token(TOKENS.BMULT, '*', TOKENS.OPERATOR))
            position += 1

        elif character == '/':
            tokens.append(Token(TOKENS.BDIV, '/', TOKENS.OPERATOR))
            position += 1

        elif character == '%':
            tokens.append(Token(TOKENS.OPERATOR, '%'))
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

        elif character == '~':
            tokens.append(Token(TOKENS.BINARYSUB, '~', TOKENS.OPERATOR))
            position += 1

        elif character.isspace():
            position += 1  # Skip whitespace

        else:
            # Skip invalid characters
            print(f"Skipping invalid character: {character}")
            position += 1

    return tokens
