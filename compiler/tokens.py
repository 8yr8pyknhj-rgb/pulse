from enum import Enum, auto


class TokenType(Enum):
    SAY = auto()
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    EQUALS = auto()
    EOF = auto()


class Token:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __repr__(self):
        if self.value is None:
            return self.type.name
        return f"{self.type.name}({self.value})"
