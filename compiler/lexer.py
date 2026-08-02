from enum import Enum, auto

class TokenType(Enum):
    SAY=auto(); IDENTIFIER=auto(); STRING=auto(); NUMBER=auto(); EQUALS=auto(); EOF=auto()

class Token:
    def __init__(self,t,v=None): self.type=t; self.value=v
    def __repr__(self): return f"{self.type.name}" if self.value is None else f"{self.type.name}({self.value})"

class Lexer:
    def __init__(self,source):
        self.source=source; self.position=0; self.tokens=[]
    def current_char(self):
        return None if self.position>=len(self.source) else self.source[self.position]
    def advance(self): self.position+=1
    def tokenize(self):
        while self.current_char() is not None:
            ch=self.current_char()
            if ch.isspace(): self.advance(); continue
            if ch=="=": self.tokens.append(Token(TokenType.EQUALS)); self.advance(); continue
            if ch=='"':
                self.advance(); s=""
                while self.current_char()!='"': s+=self.current_char(); self.advance()
                self.advance(); self.tokens.append(Token(TokenType.STRING,s)); continue
            if ch.isdigit():
                n=""
                while self.current_char() and self.current_char().isdigit(): n+=self.current_char(); self.advance()
                self.tokens.append(Token(TokenType.NUMBER,int(n))); continue
            if ch.isalpha():
                w=""
                while self.current_char() and (self.current_char().isalnum() or self.current_char()=="_"): w+=self.current_char(); self.advance()
                self.tokens.append(Token(TokenType.SAY if w=="say" else TokenType.IDENTIFIER, None if w=="say" else w)); continue
            raise Exception(f"Unknown character: {ch}")
        self.tokens.append(Token(TokenType.EOF)); return self.tokens
