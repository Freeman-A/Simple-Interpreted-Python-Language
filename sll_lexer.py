class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'


class SLL_Lexer:
    # Lexer to handle the tokenisation of the text into digestable chunks for easy parsing
    # No predefined tokens, to allow the langugae to be more flexible and easier to extend in the future
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def itter(self):
        # Itterator to loop through the text components
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def handle_whitespace(self):
        # Handle white spaces
        while self.current_char is not None and self.current_char.isspace():
            self.itter()

    def handle_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.itter()
        if self.current_char == '.':
            result += self.current_char
            self.itter()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.itter()
        return Token('NUMBER', float(result))

    def handle_identifier(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.itter()
        return Token('IDENTIFIER', result)

    def get_token(self):
        # Tokeniser
        while self.current_char is not None:
            if self.current_char.isspace():
                self.handle_whitespace()
                continue
            if self.current_char.isdigit():
                return self.handle_number()
            if self.current_char == '+':
                self.itter()
                return Token('ADD', '+')
            if self.current_char == '-':
                self.itter()
                return Token('SUB', '-')
            if self.current_char == '*':
                self.itter()
                return Token('MUL', '*')
            if self.current_char == '/':
                self.itter()
                return Token('DIV', '/')
            if self.current_char == '(':
                self.itter()
                return Token('OPAREN', '(')
            if self.current_char == ')':
                self.itter()
                return Token('CPAREN', ')')
            if self.current_char == '=':
                self.itter()
                return Token('CALC', '=')
            if self.current_char.isalpha():
                return self.handle_identifier()
            # Unknown token handling
            self.itter()
            return Token('UNKNOWN', self.current_char)
        return Token('EOF', None)
