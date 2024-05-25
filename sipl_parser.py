from sipl_lexer import Token


class AST:
    pass


class ParserError(Exception):
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Var(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Assign(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class SIPL_Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_token()

        print(self.current_token.type)

    def error(self):
        raise ParserError('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return Num(token)
        elif token.type == 'IDENTIFIER':
            self.eat('IDENTIFIER')
            return Var(token)
        elif token.type == 'OPAREN':
            self.eat('OPAREN')
            node = self.expr()
            self.eat('CPAREN')
            return node
        elif token.type == 'SUB':  # Handle unary minus
            self.eat('SUB')
            node = self.factor()
            return BinOp(Num(Token('NUMBER', 0)), Token('SUB', '-'), node)

    def term(self):
        node = self.factor()
        while self.current_token.type in ('MUL', 'DIV'):
            token = self.current_token
            if token.type == 'MUL':
                self.eat('MUL')
            elif token.type == 'DIV':
                self.eat('DIV')
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type in ('ADD', 'SUB'):
            token = self.current_token
            if token.type == 'ADD':
                self.eat('ADD')
            elif token.type == 'SUB':
                self.eat('SUB')
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def assignment(self):
        left = self.current_token
        self.eat('IDENTIFIER')
        op = self.current_token
        self.eat('CALC')
        right = self.expr()
        node = Assign(Var(left), right)
        return node

    def statement(self):
        if self.current_token.type == 'IDENTIFIER':
            current_pos = self.lexer.pos
            next_token = self.lexer.get_token()
            self.lexer.pos = current_pos
            self.lexer.current_char = self.lexer.text[current_pos]
            if next_token.type == 'CALC':
                return self.assignment()
        return self.expr()

    def parse(self):
        return self.statement()
