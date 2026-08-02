from compiler.lexer import Lexer
from compiler.parser import Parser
from compiler.interpreter import Interpreter

code = """
name = "Daniel"

say name

say "Welcome to Pulse"
"""

tokens = Lexer(code).tokenize()

tree = Parser(tokens).parse()

Interpreter().visit(tree)
