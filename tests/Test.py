from compiler.lexer import Lexer
from compiler.parser import Parser

code = """
name = "Daniel"
say name
"""

tokens = Lexer(code).tokenize()

tree = Parser(tokens).parse()

print(tree)
