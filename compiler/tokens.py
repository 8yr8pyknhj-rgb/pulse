from enum import Enum, auto


class TokenType(Enum):
    SAY = auto()
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    EQUALS = auto()
    EOF = auto()


class Token:
    def __init__(self, token_type, value=None, line=1, column=1):
        self.type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        if self.value is None:
            return f"{self.type.name}@{self.line}:{self.column}"
        return (
            f"{self.type.name}"
            f"({self.value})"
            f"@{self.line}:{self.column}"
        )
