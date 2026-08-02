# ==========================================
# Pulse AST (Abstract Syntax Tree)
# Version 0.1
# ==========================================

class Node:
    """Base class for all AST nodes."""
    pass


class Program(Node):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program({self.statements})"


class SayStatement(Node):
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"Say({self.expression})"


class Assignment(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Assign({self.name}, {self.value})"


class StringLiteral(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'String("{self.value}")'


class NumberLiteral(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class Identifier(Node):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"
class BinaryExpression(Node):

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return (
            f"Binary({self.left}, "
            f"{self.operator}, "
            f"{self.right})"
        )
