# tokenizer.py
class TOKENS:
    # Token type definitions
    NUMBER = 'NUMBER'
    BADD = 'BADD'
    BSUB = 'BSUB'
    BMULT = 'BMULT'
    BDIV = 'BDIV'
    INTEGER = 'INTEGER'
    NEGINTEGER = 'NEGINTEGER'
    FLOAT = 'FLOAT'
    ASSIGNMENT = 'ASSIGNMENT'
    BOOLEANTRUE = 'BOOLEANTRUE'
    BOOLEANFALSE = 'BOOLEANFALSE'
    EQUALITY = 'EQUALITY'
    STRING = 'STRING'
    IDENTIFIER = 'IDENTIFIER'
    TERMINATOR = 'TERMINATOR'
    OPERATOR = 'OPERATOR'
    KEYWORD = 'KEYWORD'
    SEPARATOR = 'SEPARATOR'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    COMMENT = 'COMMENT'
    WHITESPACE = 'WHITESPACE'
    NEWLINE = 'NEWLINE'
    VALUE = 'VALUE'
    EOF = 'EOF'
    VAR = 'var'
    IF = 'if'
    ELSE = 'else'
    ENDIF = 'endif'
    WHILE = 'while'
    FOR = 'for'
    AND = 'AND'
    OR = 'OR'
    NOT = 'NOT'
    FUNCTION = 'function'
    RETURN = 'return'
    UNKNOWN = 'UNKNOWN'


class Token:
    """Class representing a token with type, value, and optional superType and position."""

    def __init__(self, type, value, superType=None):
        self.type = type
        self.value = value
        self.superType = superType

    def __repr__(self):
        return f'Token({self.type}, {self.value})'
