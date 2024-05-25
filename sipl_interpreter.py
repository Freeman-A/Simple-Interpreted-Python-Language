from sipl_lexer import SIPL_Lexer, Token
from sipl_parser import SIPL_Parser, Num, BinOp, Var, Assign, ParserError


class Evaluator:
    def __init__(self):
        self.variables = {}

    def visit(self, node):
        if isinstance(node, Num):
            return self.visit_num(node)
        if isinstance(node, BinOp):
            return self.visit_binOp(node)
        if isinstance(node, Var):
            return self.visit_var(node)
        if isinstance(node, Assign):
            return self.visit_assign(node)
        if isinstance(node, ParserError):
            return self.visit_error(node)
        return None

    def visit_num(self, node):
        return node.value

    def visit_binOp(self, node):
        left_value = self.visit(node.left)
        right_value = self.visit(node.right)
        if node.op.type == 'ADD':
            result = left_value + right_value
        elif node.op.type == 'SUB':
            result = left_value - right_value
        elif node.op.type == 'MUL':
            result = left_value * right_value
        elif node.op.type == 'DIV':
            result = left_value / right_value
        return result

    def visit_var(self, node):
        var_name = node.value
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise NameError(f'Variable {var_name} not defined')

    def visit_assign(self, node):
        var_name = node.left.value
        self.variables[var_name] = self.visit(node.right)
        return self.variables[var_name]


class SIPL_Interpreter:
    def __init__(self):
        self.evaluator = Evaluator()

    def interpret(self, text):
        self.lexer = SIPL_Lexer(text)
        self.parser = SIPL_Parser(self.lexer)

        try:
            ast = self.parser.parse()
            result = self.evaluator.visit(ast)
            return result
        except Exception as e:
            return str(e)
