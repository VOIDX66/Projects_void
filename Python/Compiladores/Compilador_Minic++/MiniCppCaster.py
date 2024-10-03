# mccast.py
'''
Estructura del AST (básica). 

Debe agregar las clases que considere que hacen falta.

Statement
 |
 +--- NullStmt
 |
 +--- ExprStmt
 |
 +--- IfStmt
 |
 +--- WhileStmt
 |
 +--- ReturnStmt
 |
 +--- BreakStmt
 |
 +--- FuncDeclStmt
 |
 +--- VarDeclStmt


Expression
 |
 +--- ConstExpr                literales bool, int y float
 |
 +--- NewArrayExpr             Arreglos recien creados
 |
 +--- CallExpr                 Llamado a function
 |
 +--- VarExpr                  Variable en lado-derecho
 |
 +--- ArrayLoockupExpr         Contenido celda arreglo
 |
 +--- UnaryOpExpr              Unarios !, +, -
 |
 +--- BinaryOpExpr             Binarios ||,&&,==,!=,<,<=,>,>=,+,-,*,/,%
 |
 +--- VarAssignmentExpr        var = expr
 |
 +--- ArrayAssignmentExpr      var[expr] = expr
 |
 +--- IntToFloatExpr           Ensanchar integer a un float
 |
 +--- ArraySizeExpr            tamaño de un arreglo
'''
from dataclasses import dataclass, field
from multimethod import multimeta
from typing      import Union, List, Optional
from graphviz import *

# =====================================================================
# Clases Abstractas
# =====================================================================
@dataclass
class Visitor(metaclass=multimeta):
    '''
    Clase abstracta del Patron Visitor
    '''
    pass

@dataclass
class Node:
    def accept(self, v:Visitor, *args, **kwargs):
        return v.visit(self, *args, **kwargs)

@dataclass
class Statement(Node):
    pass

@dataclass
class Expression(Node):
    pass

# =====================================================================
# Clases Concretas
# =====================================================================
@dataclass
class Program(Statement):
    stmts : List[Statement] = field(default_factory=list)

@dataclass
class NullStmt(Statement):
    pass

@dataclass
class IfStmt(Statement):
    expr : Expression
    then : Statement
    else_: Statement = None

@dataclass
class ReturnStmt(Statement):
    expr : Expression = None

# =====================================================================
# Expresiones
# =====================================================================
@dataclass
class ConstExpr(Expression):
    value : Union[bool, int, float, str]

@dataclass
class VarExpr(Expression):
    ident : str

@dataclass
class CallExpr(Expression):
    ident : str
    args  : List[Expression] = field(default_factory=list)

@dataclass
class VarAssignmentExpr(Expression):
    ident : str
    expr  : Expression

@dataclass
class UnaryOpExpr(Expression):
    opr  : str
    expr : Expression

@dataclass
class BinaryOpExpr(Expression):
    opr : str
    left : Expression
    right : Expression
#----------------------------------------------------------------

@dataclass
class VarDeclStmt(Statement):
    type_spec : str
    ident : str
    expr: Expression = None

@dataclass
class ArrayAssignmentExpr(Expression):
    ident : str
    index : Expression
    expr  : Expression

@dataclass
class ArrayDeclStmt(Statement):
    type_spec : str
    ident: str
    size: Expression

@dataclass
class FuncDeclStmt(Statement):
    return_type : str
    ident : str
    params: List[VarDeclStmt]
    compound_stmt : List[Statement]

@dataclass
class ClassDecl(Statement):
    ident : str
    var_decl_list : List[Statement]

@dataclass
class ExprStmt(Statement):
    expr: Expression

@dataclass
class WhileStmt(Statement):
    expr : Expression
    then : Statement

@dataclass
class BreakStmt(Statement):
    break_s : Expression

@dataclass
class ContinueStmt(Statement):
    continue_s : Expression

@dataclass
class Identifier(Expression):
    name: str

@dataclass
class ArrayAccessExpr(Expression):
    ident: str
    expr: Expression

@dataclass
class ArraySizeExpr(Expression):
    ident: str
    expr: Expression

@dataclass
class LiteralExpr(Expression):
    value: Union[int, float, bool, str]

@dataclass
class NewArrayExpr(Expression):
    type_spec: str
    size: Expression

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

    # Método para visitar constantes
    def visit(self, n: ConstExpr):
        name = self.name()
        self.dot.node(name, label=f'CONST({n.value})')
        return name

    # Método para visitar variables
    def visit(self, n: VarExpr):
        name = self.name()
        self.dot.node(name, label=f'VAR({n.ident})')
        return name

    # Método para visitar llamadas a funciones
    def visit(self, n: CallExpr):
        name = self.name()
        self.dot.node(name, label=f'CALL({n.ident})')
        for arg in n.args:
            self.dot.edge(name, arg.accept(self), label='arg')
        return name

    # Método para visitar expresiones binarias
    def visit(self, n: BinaryOpExpr):
        name = self.name()
        self.dot.node(name, label=f'{n.opr}', shape='circle', color='burlywood2')
        self.dot.edge(name, n.left.accept(self), label='left')
        self.dot.edge(name, n.right.accept(self), label='right')
        return name

    # Método para visitar declaraciones de variables
    def visit(self, n: VarDeclStmt):
        name = self.name()
        self.dot.node(name, label=f'VAR_DECL({n.ident}:{n.type_spec})')
        if n.expr:
            self.dot.edge(name, n.expr.accept(self), label='init')
        if n.size:
            self.dot.edge(name, n.size.accept(self), label='size')
        return name

    # Método para visitar declaraciones de funciones
    def visit(self, n: FuncDeclStmt):
        name = self.name()
        self.dot.node(name, label=f'FUNC_DECL({n.ident}:{n.return_type})')
        for param in n.params:
            self.dot.edge(name, param.accept(self), label='param')
        for stmt in n.compound_stmt:
            self.dot.edge(name, stmt.accept(self), label='stmt')
        return name

    # Método para visitar declaraciones de clases
    def visit(self, n: ClassDecl):
        name = self.name()
        self.dot.node(name, label=f'CLASS({n.ident})')
        for stmt in n.var_decl_list:
            self.dot.edge(name, stmt.accept(self), label='var_decl')
        return name

    # Método para visitar expresiones unarias
    def visit(self, n: UnaryOpExpr):
        name = self.name()
        self.dot.node(name, label=f'{n.opr}', shape='circle', color='burlywood2')
        self.dot.edge(name, n.expr.accept(self), label='expr')
        return name

    # Método para visitar asignaciones de variables
    def visit(self, n: VarAssignmentExpr):
        name = self.name()
        self.dot.node(name, label='=', shape='circle', color='burlywood2')
        self.dot.edge(name, n.ident, label='variable')
        self.dot.edge(name, n.expr.accept(self), label='value')
        return name

    # Método para visitar un IfStmt
    def visit(self, n: IfStmt):
        name = self.name()
        self.dot.node(name, label='IF')
        self.dot.edge(name, n.expr.accept(self), label='condition')
        self.dot.edge(name, n.then.accept(self), label='then')
        if n.else_:
            self.dot.edge(name, n.else_.accept(self), label='else')
        return name

    # Método para visitar ciclos While
    def visit(self, n: WhileStmt):
        name = self.name()
        self.dot.node(name, label='WHILE')
        self.dot.edge(name, n.expr.accept(self), label='condition')
        self.dot.edge(name, n.then.accept(self), label='body')
        return name


