# ==========================================
# Pulse Parser
# Version 0.1
# ==========================================

from ast import (
    Program,
    SayStatement,
    Assignment,
    StringLiteral,
    NumberLiteral,
    Identifier,
)

from lexer import TokenType


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current(self):
        return self.tokens[self.position]

    def advance(self):
        self.position += 1

    def consume(self, token_type):

        token = self.current()

        if token.type != token_type:
            raise Exception(
                f"Expected {token_type}, got {token.type}"
            )

        self.advance()

        return token

    def parse(self):

        statements = []

        while self.current().type != TokenType.EOF:

            statements.append(
                self.statement()
            )

        return Program(statements)

    def statement(self):

        token = self.current()

        if token.type == TokenType.SAY:
            return self.say_statement()

        if token.type == TokenType.IDENTIFIER:
            return self.assignment()

        raise Exception(
            f"Unexpected token: {token}"
        )

    def say_statement(self):

        self.consume(TokenType.SAY)

        value = self.expression()

        return SayStatement(value)

    def assignment(self):

        name = self.consume(
            TokenType.IDENTIFIER
        )

        self.consume(TokenType.EQUALS)

        value = self.expression()

        return Assignment(
            name.value,
            value
        )

    def expression(self):

        token = self.current()

        if token.type == TokenType.STRING:

            self.advance()

            return StringLiteral(token.value)

        if token.type == TokenType.NUMBER:

            self.advance()

            return NumberLiteral(token.value)

        if token.type == TokenType.IDENTIFIER:

            self.advance()

            return Identifier(token.value)

        raise Exception(
            f"Unexpected expression: {token}"
        )
