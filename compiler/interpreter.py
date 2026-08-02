# interpreter.py
from compiler.ast import (
    Program,
    SayStatement,
    Assignment,
    StringLiteral,
    NumberLiteral,
    Identifier,
)


class Interpreter:

    def __init__(self):
        self.variables = {}

    def visit(self, node):

        if isinstance(node, Program):
            return self.visit_program(node)

        if isinstance(node, SayStatement):
            return self.visit_say(node)

        if isinstance(node, Assignment):
            return self.visit_assignment(node)

        if isinstance(node, StringLiteral):
            return node.value

        if isinstance(node, NumberLiteral):
            return node.value

        if isinstance(node, Identifier):
            return self.variables[node.name]

        raise Exception(f"Unknown node: {type(node)}")

    def visit_program(self, program):

        for statement in program.statements:
            self.visit(statement)

    def visit_say(self, statement):

        value = self.visit(statement.expression)

        print(value)

    def visit_assignment(self, statement):

        value = self.visit(statement.value)

        self.variables[statement.name] = value
