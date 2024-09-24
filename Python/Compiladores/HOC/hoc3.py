#Instalamos las librerias requeridas
#pip install -r requirements.txt

from dataclasses import dataclass
import re
from graphviz import Digraph
from multimethod import multimeta
from typing import Union
from rich import print
import math

@dataclass
class Token:
    type: str
    value: str
    lineno: int = 1

class Lexer:
    
    tokens = [
        (r'\n+', lambda s, tok: Token('NEWLINE', tok)),
        (r'\s+', None),  # Ignorar espacios en blanco
        # Def de tokens
        (r'PI', lambda s, tok: Token('NUMBER', '3.14159265358979323846')),
        (r'E', lambda s, tok: Token('NUMBER', '2.71828182845904523536')),
        (r'GAMMA', lambda s, tok: Token('NUMBER', '0.57721566490153286060')),
        (r'DEG', lambda s, tok: Token('NUMBER', '57.29577951308232087680')),
        (r'PHI', lambda s, tok: Token('NUMBER', '1.61803398874989484820')),
        (r'\d+(\.\d+)?', lambda s, tok: Token('NUMBER', tok)),
        # Definición de funciones matemáticas como tokens
        (r'sin', lambda s, tok: Token('FUNCTION', 'sin')),
        (r'cos', lambda s, tok: Token('FUNCTION', 'cos')),
        (r'atan', lambda s, tok: Token('FUNCTION', 'atan')),
        (r'exp', lambda s, tok: Token('FUNCTION', 'exp')),
        (r'log', lambda s, tok: Token('FUNCTION', 'log')),
        (r'log10', lambda s, tok: Token('FUNCTION', 'log10')),
        (r'sqrt', lambda s, tok: Token('FUNCTION', 'sqrt')),
        (r'int', lambda s, tok: Token('FUNCTION', 'int')),
        (r'abs', lambda s, tok: Token('FUNCTION', 'abs')),
        (r'[a-zA-Z_]\w*',lambda s, tok: Token('IDENT', tok)),
        # Definicion de tokens operaciones
        (r'\+', lambda s, tok: Token('+', tok)),
        (r'-', lambda s, tok: Token('-', tok)),
        (r'\*', lambda s, tok: Token('*', tok)),
        (r'/', lambda s, tok: Token('/', tok)),
        (r'\^', lambda s, tok: Token('^', tok)),
        (r'=', lambda s, tok: Token('=', tok)),
        (r'\(', lambda s, tok: Token('(', tok)),
        (r'\)', lambda s, tok: Token(')', tok)),
        # Manejo de errores
        (r'.', lambda s, tok: print(f"Ilegal Charater: '{tok}'")),
    ]

    def tokenize(self, data):
        scanner = re.Scanner(self.tokens)
        results, remainder = scanner.scan(data)
        
        # Inicializa el número de línea
        line_number = 1
        tokens_with_lines = []

        for token in results:
            if token.type == 'NEWLINE':
                line_number += 1
            elif token.type:
                # Crea el token con el número de línea actual
                mytoken = Token(token.type, token.value, line_number)
                tokens_with_lines.append(mytoken)

        if remainder:
            print(f"Error: No se pudo escanear completamente: {remainder}")

        print(tokens_with_lines)
        return iter(tokens_with_lines)

class Visitor(metaclass=multimeta):
    pass

# NODOS---------------------------------------------------------------------

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
class Function(Expression):
    func: str
    expr: Expression

@dataclass
class Unary(Expression):
    oper: str
    expr: Expression

@dataclass
class Binary(Expression):
    oper: str
    left: Expression
    right: Expression

@dataclass
class Assignment(Statement):
    loc: Expression
    expr: Expression

@dataclass
class Identifier(Expression):
    name: str

@dataclass
class Number(Expression):
    value: Union[float, int]

# MakeDot ----------------------------------------------------------------
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
    
    # Método para visitar funciones matemáticas
    def visit(self, n: Function):
        name = self.name()
        self.dot.node(name, label=f'{n.func}', shape='circle', color='burlywood2')
        self.dot.edge(name, n.expr.accept(self), label='expr')
        return name

    # Método para visitar operaciones binarias
    def visit(self, n: Binary):
        name = self.name()
        self.dot.node(name, label=f'{n.oper}', shape='circle', color='burlywood2')
        self.dot.edge(name, n.left.accept(self), label='left')
        self.dot.edge(name, n.right.accept(self), label='right')
        return name

    # Método para visitar operaciones unarias
    def visit(self, n: Unary):
        name = self.name()
        self.dot.node(name, label=f'{n.oper}', shape='circle', color='burlywood2')
        self.dot.edge(name, n.expr.accept(self), label='expr')
        return name
    
    # Método para visitar identificadores
    def visit(self, n: Identifier):
        name = self.name()
        self.dot.node(name, label=f'IDENT({n.name})')
        return name

    # Método para visitar asignaciones
    def visit(self, n: Assignment):
        name = self.name()
        # Crear un nodo para la asignación, que muestra el símbolo '='
        self.dot.node(name, label='=', shape='circle', color='burlywood2')

        # Conectar el nodo de asignación con el identificador (variable) y la expresión
        self.dot.edge(name, n.loc.accept(self), label='variable')
        self.dot.edge(name, n.expr.accept(self), label='value')

        return name

# PARSER ----------------------------------------------------------------
class Evaluator(Visitor):
    def __init__(self):
        self.variables = dict()

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
        elif n.oper == '^':
            return left ** right
        else:
            raise ValueError(f"Operador desconocido: {n.oper}")

    def visit(self, n: Unary):
        expr_value = n.expr.accept(self)

        if n.oper == '-':
            return -expr_value
        else:
            raise ValueError(f"Operador unario desconocido: {n.oper}")

    def visit(self, n: Number):
        return n.value
    
    def visit(self, node):
        if isinstance(node, Function):
            value = node.expr.accept(self)
            if node.func == 'sin':
                return math.sin(value)
            elif node.func == 'cos':
                return math.cos(value)
            elif node.func == 'atan':
                return math.atan(value)
            elif node.func == 'exp':
                return math.exp(value)
            elif node.func == 'log':
                return math.log(value)
            elif node.func == 'log10':
                return math.log10(value)
            elif node.func == 'sqrt':
                return math.sqrt(value)
            elif node.func == 'int':
                return int(value)
            elif node.func == 'abs':
                return abs(value)
            else:
                raise ValueError(f"Función desconocida: {node.func}")
    
    def visit(self, n: Identifier):
        #print(f"Buscando {n.name}")
        if n.name in self.variables:
            return self.variables[n.name]
        else:
            raise NameError(f"Variable '{n.name}' no definida")
        
    def visit(self, n: Assignment):
        value = n.expr.accept(self)
        self.variables[n.loc.name] = value
        print(f"{n.loc.name} = {value}")
        return value

class RecursiveDescentParser:
    def assignment(self):
		# assignment : IDENT = expression | expression
        if self._accept('IDENT'):
            name = Identifier(self.tok.value)
            self._expect('=')
            expr = self.expression()
            return Assignment(name, expr), 0
        else:
            return self.expression(), 1

    def expression(self):
        # expression : term { ('+'|'-') term }
        expr = self.term()
        while self._accept('+') or self._accept('-'):
            oper = self.tok.value
            right = self.term()
            expr = Binary(oper, expr, right)
        return expr

    def term(self):
        # term : factor { ('*'|'/'|'^') factor }
        term = self.factor()
        while self._accept('*') or self._accept('/') or self._accept('^'):
            oper = self.tok.value
            right = self.factor()
            term = Binary(oper, term, right)
        return term

    def function(self):
        func_name = self.tok.value  # Obtiene el nombre de la función
        self._accept('(')
        expr = self.expression()  # Asumimos que las funciones solo tienen un argumento
        self._accept(')')
        return Function(func_name, expr)  # Devuelve un nodo Function con el nombre y la expresión
    
    def factor(self):
        # factor : IDENT | '-' | NUMBER | ( expression )
        if self._accept('IDENT'):
            return Identifier(self.tok.value)
        elif self._accept('-'):
            return Unary('-', self.factor())
        elif self._accept('NUMBER'):
            node_number = Number(float(self.tok.value))
            # Verificar si después de un número viene un paréntesis sin un operador
            if self._accept("("):
                raise SyntaxError("Falta un operador entre el número y el paréntesis")
            return node_number
        elif self._accept('('):
            expr = self.expression()
            self._expect(')')
            return expr
        elif self._accept('FUNCTION'):
            return self.function()
        elif self._accept('NEWLINE'):
            pass
        else:
            raise SyntaxError('Esperando NUMBER o (')

    # FUNCIONES DE UTILIDAD ----------------------------------------------------------------
    def _advance(self):
        'Advanced the tokenizer by one symbol'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Consume the next token if it matches an expected type'
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
        evaluator = Evaluator() #Evaluar la expresion
        while self.nexttok is not None:
            expr, type = self.assignment()
            # Mostrar el resultado
            if expr:
                result = expr.accept(evaluator)
                if type == 0:
                    pass
                else:
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

# Ejecutar 

data = '''
1.5^2.3
exp(2.3*log(1.5))
sin(PI/2)
atan(1)*DEG
'''

lexer = Lexer()
parser = RecursiveDescentParser()

asts = parser.parse(lexer.tokenize(data))

#Arbol de sintaxis abstracto

for num , ast in enumerate(asts):
    # Visualización
    dot_visitor = MakeDot()
    ast.accept(dot_visitor)
    #Guardamos en formato png
    dot_visitor.dot.render(filename=f'HOC 3 AST {num}', format='png', cleanup=True)
