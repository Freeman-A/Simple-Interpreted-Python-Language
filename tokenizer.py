# tokenizer.py

class TOKENS:
    # Token type definitions
    GREATER = 'GREATER'  # Greater than '>'
    GREATEREQUAL = 'GREATEREQUAL'  # Greater than or equal to '>='
    LESS = 'LESS'  # Less than '<'
    LESSEQUAL = 'LESSEQUAL'  # Less than or equal to '<='
    NUMBER = 'NUMBER'  # Generic number token
    BADD = 'BADD'  # Binary addition '+'
    BSUB = 'BSUB'  # Binary subtraction '-'
    BMULT = 'BMULT'  # Binary multiplication '*'
    BDIV = 'BDIV'  # Binary division '/'
    INTEGER = 'INTEGER'  # Integer number
    NEGINTEGER = 'NEGINTEGER'  # Negative integer
    FLOAT = 'FLOAT'  # Floating-point number
    ASSIGNMENT = 'ASSIGNMENT'  # Assignment '='
    BOOLEANTRUE = 'BOOLEANTRUE'  # Boolean true 'true'
    BOOLEANFALSE = 'BOOLEANFALSE'  # Boolean false 'false'
    EQUALITY = 'EQUALITY'  # Equality '=='
    NOTEQUAL = 'NOTEQUAL'  # Not equal '!='
    STRING = 'STRING'  # String literal
    IDENTIFIER = 'IDENTIFIER'  # Identifier (e.g., variable name)
    TERMINATOR = 'TERMINATOR'  # Statement terminator (e.g., ';')
    OPERATOR = 'OPERATOR'  # Operator
    KEYWORD = 'KEYWORD'  # Keyword (e.g., 'if', 'while')
    SEPARATOR = 'SEPARATOR'  # Separator (e.g., ',')
    LPAREN = 'LPAREN'  # Left parenthesis '('
    RPAREN = 'RPAREN'  # Right parenthesis ')'
    COMMENT = 'COMMENT'  # Comment
    WHITESPACE = 'WHITESPACE'  # Whitespace
    NEWLINE = 'NEWLINE'  # Newline
    VALUE = 'VALUE'  # Generic value
    EOF = 'EOF'  # End of file/input
    VAR = 'VAR'  # Variable declaration 'var'
    IF = 'IF'  # If statement 'if'
    ELSE = 'ELSE'  # Else statement 'else'
    ENDIF = 'ENDIF'  # End if statement 'endif'
    WHILE = 'WHILE'  # While loop 'while'
    FOR = 'FOR'  # For loop 'for'
    AND = 'AND'  # Logical AND 'and'
    OR = 'OR'  # Logical OR 'or'
    NOT = 'NOT'  # Logical NOT 'not'
    FUNCTION = 'FUNCTION'  # Function declaration 'function'
    RETURN = 'RETURN'  # Return statement 'return'
    UNKNOWN = 'UNKNOWN'  # Unknown token


class Token:
    """Class representing a token with type, value, and optional superType and position."""

    def __init__(self, type, value, superType=None):
        """
        Initialize the token.

        Parameters:
        type (str): The type of the token (e.g., IDENTIFIER, INTEGER).
        value (str): The value of the token.
        superType (str): The super type of the token (optional).
        """
        self.type = type
        self.value = value
        self.superType = superType

    def __repr__(self):
        """
        String representation of the token.

        Returns:
        str: The string representation of the token.
        """
        return f'Token({self.type}, {self.value})'
