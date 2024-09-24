from dataclasses import dataclass
import re 
from graphviz import Digraph
from typing import Union
from rich import print

@dataclass
class Token:
    type: str
    value: str

class Lexer:
    tokens = [
        # ignore
        (r'\s+', None),
        # Def de tokens
        (r'\d+(\.\d+)?(E[+-]?\d+)?', lambda s, tok: Token('NUMBER', tok)),
        (r'[a-zA-Z_]\w*',            lambda s, tok: Token('IDENT', tok)),
        (r'\+',                      lambda s, tok: Token('+', tok)),
        (r'-',                       lambda s, tok: Token('-', tok)),
        (r'\*',                      lambda s, tok: Token('*', tok)),
        (r'/',                       lambda s, tok: Token('/', tok)),
        (r'=',                       lambda s, tok: Token('=', tok)),
        (r'\(',                      lambda s, tok: Token('(', tok)),
        (r'\)',                      lambda s, tok: Token(')', tok)),
        #Manejo de errores
        (r'.',                       lambda s, tok: print(f"Ilegal Charater: '{tok}'")),   
    ]

    def tokenize(self, data):
        scanner = re.Scanner(self.tokens)
        result, remainer = scanner.scan(data)

        return iter(result)

 

@dataclass
class Node:
    pass

#Nodo tipo instruccion
@dataclass
class Statement(Node):
    pass

#Nodo tipo expresion
@dataclass
class Expression(Node):
    pass

@dataclass
class Assingment(Statement):
    loc: Expression
    expr: Expression

@dataclass
class Binary(Expression):
    oper: str
    left: Expression
    right: Expression

@dataclass
class Identifier(Expression):
    name: str

@dataclass
class Number(Expression):
    value: Union[float, int]



class RecursiveDescentParser:
    def assignment(self):
        if self._accept('IDENT'):
            name = Identifier(self.tok.value)
            self._expect('=')
            expr = self.expression()
            return Assingment(name, expr)
        else:
            raise SyntaxError("Se esperaba un 'IDENT'")

    def expression(self):
        expr = self.term()
        while self._accept('+') or self._accept('-'):
            oper = self.tok.value
            right = self.term()
            expr = Binary(oper, expr, right)
        return expr

    def term(self):
        term = self.factor()
        while self._accept('*') or self._accept('/'):
            oper = self.tok.value
            right = self.factor()
            term = Binary(oper, term, right)
        return term

    def factor(self):
        if self._accept('IDENT'):
            return Identifier(self.tok.value)
        elif self._accept('NUMBER'):
            return Number(self.tok.value)
        elif self._accept('('):
            expr = self.expression()
            self._expect(')')
            return expr
        else:
            raise SyntaxError("Se esperaba un 'IDENT' o 'NUMBER' o '('")

    def _advance(self):
        #'Advanced the tokenizer by one symbol'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self,toktype):
        #'Consume the next token if it matches an expected type'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self,toktype):
        'Consume and discard the next token or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError("Expected %s" % toktype)

    def start(self):
        'Entry point to parsing'
        self._advance()              # Load first lookahead token
        return self.assignment()

    def parse(self,tokens):
        'Entry point to parsing'
        self.tok = None         # Last symbol consumed
        self.nexttok = None     # Next symbol tokenized
        self.tokens = tokens
        return self.start()
    
data = 'x = 3 + 42 * (s - t)'

try:
  lexer  = Lexer()
  parser = RecursiveDescentParser()

  top = parser.parse(lexer.tokenize(data))

  print(top)
except SystemError as err:
  print(err)