#Instalamos las librerias requeridas
#pip install -r requirements.txt


from dataclasses import dataclass
import re
from graphviz import Digraph
from multimethod import multimeta
from typing import Union
from rich import print

@dataclass
class Token:
    type: str
    value: str
    lineno: int = 1

class Lexer:
    #Definimos los tokens
    tokens = [
        (r'\n+', lambda s, tok: Token('NEWLINE', tok)),
        (r'\s+', None),  # Ignorar espacios en blanco
        # Def de tokens
        (r'\d+(\.\d+)?', lambda s, tok: Token('NUMBER', tok)),
        (r'\+', lambda s, tok: Token('+', tok)),
        (r'-', lambda s, tok: Token('-', tok)),
        (r'\*', lambda s, tok: Token('*', tok)),
        (r'/', lambda s, tok: Token('/', tok)),
        (r'=', lambda s, tok: Token('=', tok)),
        (r'\(', lambda s, tok: Token('(', tok)),
        (r'\)', lambda s, tok: Token(')', tok)),
        # Manejo de errores
        (r'.', lambda s, tok: print(f"Ilegal Charater: '{tok}'")),
    ]

    def tokenize(self, data):
        scanner = re.Scanner(self.tokens)
        results, remainder = scanner.scan(data)

        if remainder:
            print(f"Error: No se pudo escanear completamente: {remainder}")

        print(results)
        return iter(results)

class Visitor(metaclass=multimeta):
    pass

@dataclass
class Node:
    def accept(self, v: Visitor):
        return v.visit(self)

# Nodo tipo instruccion
@dataclass
class Statement(Node):
    pass

# Nodo tipo expresion
@dataclass
class Expression(Node):
    pass

# Expresiones
@dataclass
class Binary(Expression):
    oper: str
    left: Expression
    right: Expression

@dataclass
class Number(Expression):
    value: Union[float, int]

# MakeDot
class MakeDot(Visitor):
    node_default = {
        'shape': 'box',
        'color': 'coral2',
        'style': 'filled',
    }
    edge_default = {
        'arrowhead': 'none'
    }

    def __init__(self):
        self.dot = Digraph('AST')
        self.dot.attr('node', **self.node_default)
        self.dot.attr('edge', **self.edge_default)
        self.seq = 0

    def name(self):
        self.seq += 1
        return f'n{self.seq}'

    # Método para visitar números
    def visit(self, n: Number):
        name = self.name()
        self.dot.node(name, label=f'NUMBER({n.value})')
        return name

    # Método para visitar operaciones binarias
    def visit(self, n: Binary):
        name = self.name()
        self.dot.node(name, label=f'{n.oper}', shape='circle', color='burlywood2')
        self.dot.edge(name, n.left.accept(self), label='left')
        self.dot.edge(name, n.right.accept(self), label='right')
        return name

# PARSER
class Evaluator(Visitor):
    def visit(self, n: Binary):
        left = n.left.accept(self)
        right = n.right.accept(self)

        if n.oper == '+':
            return left + right
        elif n.oper == '-':
            return left - right
        elif n.oper == '*':
            return left * right
        elif n.oper == '/':
            return left / right
        else:
            raise ValueError(f"Operador desconocido: {n.oper}")

    def visit(self, n: Number):
        return n.value

class RecursiveDescentParser:
    def expression(self):
        # expression : term { ('+'|'-') term }
        expr = self.term()
        while self._accept('+') or self._accept('-'):
            oper = self.tok.value
            right = self.term()
            expr = Binary(oper, expr, right)
        return expr

    def term(self):
        # term : factor { ('*'|'/') factor }
        term = self.factor()
        while self._accept('*') or self._accept('/'):
            oper = self.tok.value
            right = self.factor()
            term = Binary(oper, term, right)
        return term

    def factor(self):
        # factor : NUMBER | ( expression )
        if self._accept('NUMBER'):
            node_number = Number(float(self.tok.value))
            # Verificar si después de un número viene un paréntesis sin un operador
            if self._accept('('):
                raise SyntaxError("Falta un operador entre el número y el paréntesis")
            return node_number
        elif self._accept('('):
            expr = self.expression()
            self._expect(')')
            return expr
        elif self._accept('NEWLINE'):
            pass
        else:
            raise SyntaxError("Se esperaba un NUMBER o '('")

    # FUNCIONES DE UTILIDAD
    def _advance(self):
        # 'Advanced the tokenizer by one symbol'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        # 'Consume the next token if it matches an expected type'
        proximo = self.nexttok
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume and discard the next token or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError("Expected %s" % toktype)

    def start(self):
        'Punto de entrada al análisis'
        self._advance()  # Cargar el primer token de anticipación
        ast_nodes = []
        while self.nexttok is not None:
            expr = self.expression()  # Analizar una expresión

            # Evaluar la expresión y mostrar el resultado
            evaluator = Evaluator()
            if expr:
                result = expr.accept(evaluator)
                print(f"Resultado: {result}")

                ast_nodes.append(expr)

            # Avanzar al siguiente token. Si hay salto de línea, ignorarlo
            if self._accept('NEWLINE'):
                continue  # Saltar a la siguiente expresión después del salto de línea
            elif not self.nexttok:
                break  # Terminar si no hay más tokens

        return ast_nodes

    def parse(self, tokens):
        'Entry point to parsing'
        self.tok = None  # Last symbol consumed
        self.nexttok = None  # Next symbol tokenized
        self.tokens = tokens
        return self.start()

data = '''
4*3*2
(1+2) * (3+4)
1/2
355/113
'''
#-3-4 Error aun no existe el unary minus

lexer = Lexer()
parser = RecursiveDescentParser()

asts = parser.parse(lexer.tokenize(data))

#Arbol de sintaxis abstracto

for num , ast in enumerate(asts):
    # Visualización
    dot_visitor = MakeDot()
    ast.accept(dot_visitor)
    dot_visitor.dot.render(filename=f'HOC 1 AST {num}', format='png', cleanup=True)