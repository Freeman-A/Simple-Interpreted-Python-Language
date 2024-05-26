# variable.py
from dataclasses import dataclass
from tokenizer import TOKENS, Token

globalVariables = {}


@dataclass
class Variable:
    name: str
    hasValue: bool = False
    strValue: str = ''
    intValue: int = 0
    floatValue: float = 0.0
    type: TOKENS = TOKENS.VALUE
    superType: TOKENS = TOKENS.VALUE

    def __repr__(self):
        return self.strValue

    def update(self):
        if self.type == TOKENS.INTEGER:
            self.strValue = str(self.intValue)
            self.floatValue = 0.0
        elif self.type == TOKENS.FLOAT:
            self.strValue = str(self.floatValue)
            self.intValue = 0
        else:
            self.intValue = 0
            self.floatValue = 0.0
