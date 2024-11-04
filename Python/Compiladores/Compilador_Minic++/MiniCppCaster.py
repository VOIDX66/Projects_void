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
class CompoundStmt(Statement):
    stmts : List[Statement] = field(default_factory=list)

@dataclass
class IfStmt(Statement):
    expr : Expression
    then : CompoundStmt
    else_: CompoundStmt = None

@dataclass
class ReturnStmt(Statement):
    expr : Expression

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
    var : Expression
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
    size : Expression = None

@dataclass
class ArrayAssignmentExpr(Expression):
    ident : str
    index : Expression
    expr  : Expression

@dataclass
class FuncDeclStmt(Statement):
    return_type : str
    ident : str
    params: List[VarDeclStmt]
    compound_stmt : CompoundStmt#List[Statement]

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
    then : CompoundStmt

@dataclass
class ForStmt(Statement):
    init: Expression  
    cond: Expression  
    update: Expression 
    then: CompoundStmt  

@dataclass
class BreakStmt(Statement):
    pass

@dataclass
class ContinueStmt(Statement):
    pass

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
class IOFuncExpr(Expression):
    ident: str
    args: List[Expression] = field(default_factory=list)

@dataclass
class CastExpr(Expression):
    type_spec: str
    expr: Expression

@dataclass
class NewArrayExpr(Expression):
    type_spec: str
    size: Expression

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
    
    # Método para nodos no definidos
    def visit_default(self, node):
        name = self.name()
        node_type = type(node).__name__
        self.dot.node(name, label=f'UNDEFINED_NODE({node_type})')
        print(f"Advertencia: Nodo de tipo '{node_type}' no tiene un método de visita definido.")
        return name

    # Metodo
    def visit(self, n: Program):
        '''
        1.
            - Crear tabla de simbolos global   
            - Agregar todas las funciones o variables incorporadas al lenguaje:
                scanf/printf
            - Despues de recorer el AST validar que exista una funcon main
        2.
            Guardar la tabla de simbolos actual
        
        3. 
            FuncDeclStmt
            -Agregar el nombre de la funcion a la TS actual
        '''
        name = self.name()  # Crea un nombre para el nodo del programa
        self.dot.node(name, label='PROGRAM')  # Agrega el nodo al gráfico
        for stmt in n.stmts:  # Itera sobre las declaraciones en el programa
            self.dot.edge(name, stmt.accept(self), label='stmt')  # Agrega una arista para cada declaración
        return name

    # Método para visitar constantes
    def visit(self, n: ConstExpr):
        name = self.name()
        self.dot.node(name, label=f'CONST({n.value})')
        return name

    # Método para visitar declaraciones de clases
    def visit(self, n: ClassDecl):
        name = self.name()
        self.dot.node(name, label=f'CLASS({n.ident})')
        for stmt in n.var_decl_list:
            self.dot.edge(name, stmt.accept(self), label='var_decl')
        return name

    def visit(self, n: CompoundStmt):
        name = self.name()
        self.dot.node(name, label='COMPOUND_STATEMENT')
        for stmt in n.stmts:
            self.dot.edge(name, stmt.accept(self), label='stmt')
        return name

    # Método para visitar declaraciones de funciones
    def visit(self, n: FuncDeclStmt):
        name = self.name()
        self.dot.node(name, label=f'FUNC_DECL({n.ident}:{n.return_type})')
        self.dot.edge(name, n.compound_stmt.accept(self), label='compund_stmts')
        for param in n.params:
            self.dot.edge(name, param.accept(self), label='param')
        #for stmt in n.compound_stmt:
        #    self.dot.edge(name, stmt.accept(self), label='stmt')
        return name
    
    # Método para visitar declaraciones de variables
    def visit(self, n: VarDeclStmt):
        name = self.name()
        if n.size:
            self.dot.node(name, label=f'VAR_DECL({n.ident}:{n.type_spec}[{n.size}])')
        else:
            self.dot.node(name, label=f'VAR_DECL({n.ident}:{n.type_spec})')
            if n.expr:
                self.dot.edge(name, n.expr.accept(self), label='init')
        return name    
    
    # Método para visitar variables
    def visit(self, n: VarExpr):
        name = self.name()
        self.dot.node(name, label=f'VAR({n.ident})')
        return name

    # Método para visitar asignaciones de variables
    def visit(self, n: VarAssignmentExpr):
        name = self.name()
        self.dot.node(name, label='=', shape='circle', color='burlywood2')
        self.dot.edge(name, n.var.accept(self))
        self.dot.edge(name, n.expr.accept(self), label='assign_expr')
        return name


    # Método para visitar un IfStmt
    def visit(self, n: IfStmt):
        name = self.name()
        self.dot.node(name, label='IF')
        self.dot.edge(name, n.expr.accept(self), label='condition')
        #for then_stmt in n.then:
        #    self.dot.edge(name, then_stmt.accept(self), label='then')
        self.dot.edge(name, n.then.accept(self), label='then_stmts')
        if n.else_:
            self.dot.edge(name, n.else_.accept(self), label='else_stmts')
        #    for else_stmt in n.else_:
        #        self.dot.edge(name, else_stmt.accept(self), label='else')
        return name

    # Método para visitar ciclos While
    def visit(self, n: WhileStmt):
        name = self.name()
        self.dot.node(name, label='WHILE')
        #for body_stmt in n.then:  # Asumiendo que stmt.then es una lista de declaraciones
        #    self.dot.edge(name, body_stmt.accept(self), label='body')
        self.dot.edge(name, n.expr.accept(self), label='condition')
        self.dot.edge(name, n.then.accept(self), label='then_stmts')
        return name

    # Método para visitar ciclos For
    def visit(self, n: ForStmt):
        name = self.name()
        self.dot.node(name, label='FOR')
        
        # Conecta la inicialización
        if n.init:
            self.dot.edge(name, n.init.accept(self), label='init')
        
        # Conecta la condición
        self.dot.edge(name, n.cond.accept(self), label='condition')
        
        # Conecta la actualización
        if n.update:
            self.dot.edge(name, n.update.accept(self), label='update')
        
        # Conecta el cuerpo del bucle
        #for body_stmt in n.then:  # Asumiendo que `then` es una lista de declaraciones
        #    self.dot.edge(name, body_stmt.accept(self), label='body')
        self.dot.edge(name, n.then.accept(self), label='then_stmts')
        return name
        
        return name
    
    # Método para visitar el nodo BreakStmt
    def visit(self, n: BreakStmt):
        name = self.name()
        self.dot.node(name, label='BREAK')
        return name

    # Método para visitar el nodo ContinueStmt
    def visit(self, n: ContinueStmt):
        name = self.name()
        self.dot.node(name, label='CONTINUE')
        return name

    # Método para visitar expresiones de entrada/salida
    def visit(self, n: IOFuncExpr):
        name = self.name()
        if n.ident == 'printf':
            self.dot.node(name, label='PRINTF')
        elif n.ident == 'scanf':
            self.dot.node(name, label='SCANF')
        
        for arg in n.args:
            self.dot.edge(name, arg.accept(self), label='arg')
        
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

    # Método para visitar expresiones unarias
    def visit(self, n: UnaryOpExpr):
        name = self.name()
        self.dot.node(name, label=f'{n.opr}', shape='circle', color='burlywood2')
        self.dot.edge(name, n.expr.accept(self), label='expr')
        return name

    # Método para visitar expresiones literales
    def visit(self, n: LiteralExpr):
        name = self.name()  # Genera un nombre único para el nodo
        self.dot.node(name, label=f'LITERAL({n.value})')  # Usa el valor literal
        return name
    
    # Método para visitar declaraciones de retorno
    def visit(self, n: ReturnStmt):
        name = f'return_stmt_{id(n.expr)}'
        self.dot.node(name, 'return')
        self.dot.edge(name, n.expr.accept(self), label='expr')
        return name

    def visit(self, n: ExprStmt):
        name = f'expr_stmt_{id(n.expr)}'
        self.dot.node(name, 'expr_stmt') 
        self.dot.edge(name, n.expr.accept(self), label='expr')  # Suponiendo que `stmt.expr` es una expresión válida
        return name
    
    def visit(self, n: CastExpr):
        name = f'cast_stmt_{id(n.expr)}'
        self.dot.node(name, 'cast_stmt')
        self.dot.edge(name, n.type_spec, label='type_spec')
        self.dot.edge(name, n.expr.accept(self), label='expr')
        return name