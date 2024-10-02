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
from typing      import Union, List

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

#----------------------------------------------------------------

@dataclass
class VarDeclStmt(Statement):
    type_spec : str
    ident : str
    #is_array: bool = false
    expr: Expression = None
    size: Expression = None

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