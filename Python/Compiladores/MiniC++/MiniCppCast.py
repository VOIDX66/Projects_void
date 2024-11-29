from dataclasses import *
from typing import Any, List
from multimethod import multimeta
from graphviz import *

@dataclass
class Visitor(metaclass=multimeta):
    pass

@dataclass
class Node():
    def accept(self, vis: Visitor):
        return vis.visit(self)

@dataclass
class Statement(Node):
    pass

@dataclass
class Expression(Node):
    pass

@dataclass
class Declaration(Statement):
    pass

@dataclass
class ClassDeclaration(Declaration):
    name   : str
    sclass : str
    methods: List[Statement] = field(default_factory=list)


@dataclass
class FuncDeclaration(Declaration):
    name   : str
    parameters: List[Expression] = field(default_factory=list)
    stmts  : List[Statement] = field(default_factory=list)

@dataclass
class VarDeclaration(Declaration):
    name   : str
    expr   : Expression

@dataclass
class Program(Statement):
    decl   : List[Statement] = field(default_factory=list)

@dataclass
class Print(Statement):
    expr   : Expression

@dataclass
class IfStmt(Statement):
    cond   : Expression
    cons   : List [Statement]=field(default_factory=list)
    altr   : List [Statement]=field(default_factory=list)

@dataclass
class WhileStmt(Statement):
    cond  : Expression
    body  : List[Statement]=field(default_factory=list)

@dataclass
class ForStmt(Statement):
    for_init : Expression
    for_cond : Expression
    for_increment : Expression
    for_body : List[Statement]=field(default_factory=list)

@dataclass
class Return(Statement):
    expr  : Expression

@dataclass
class ExprStmt(Statement):
    expr  : Expression

@dataclass
class Expr(Statement):
    stmts :  List[Statement] = field(default_factory=list)

@dataclass
class Continue(Statement):
    name   : str

@dataclass
class Break(Statement):
    name   : str

@dataclass
class Literal(Expression):
    value  : Any

@dataclass
class Binary(Expression): 
    op     : str
    left   : Expression
    right  : Expression

@dataclass
class Logical(Expression):
    op     : str       
    left   : Expression
    right  : Expression

@dataclass
class Unary(Expression):
    op     : str       
    expr   : Expression

@dataclass
class Grouping(Expression):
    expr  : Expression

@dataclass
class Variable(Expression):
    name   : str

@dataclass
class Assign(Expression):
    op     : str
    name   : str
    expr   : Expression

@dataclass
class AssignPostfix(Expression):
    op     : str
    expr   : Expression

@dataclass
class AssignPrefix(Expression):
    op     : str
    expr   : Expression

@dataclass
class Call(Expression):
    func  : Expression
    args  : List[Expression]=field(default_factory=list)

@dataclass
class Set(Expression):
    obj   : str
    name  : str
    expr  : Expression

@dataclass
class Get(Expression):
    obj   : str
    name  : str

@dataclass
class Super(Expression):
    name   : str

@dataclass
class List(Expression):
    name   : str

@dataclass
class This(Expression):
    pass

class MakeDot(Visitor):

    node_default = {
        'shape': 'box',
        'color': 'lightskyblue',
        'style': 'filled',
        'fontname': 'Helvetica',
    }
    edge_defaults = {
        'arrowhead': 'vee',
        'color': 'gray50',
    }
    color = 'dodgerblue3'

    def __init__(self):
        self.dot = Digraph('AST')

        self.dot.attr('node', **self.node_default)
        self.dot.attr('edge', **self.edge_defaults)
        self.program = False
        self.seq = 0
        self.cont = 0

    def __repr__(self):
        return self.dot.source

    def __str__(self):
        return self.dot.source

    @classmethod
    def render(cls, model):
        dot = cls()
        model.accept(dot)
        return dot.dot

    def name(self):
        self.seq += 1
        return f'n{self.seq:02d}'

    # nodos de Declaration

    def visit(self, node : ClassDeclaration):
        name = self.name()
        self.dot.node(name, label=fr"ClassDeclaration\nname='{node.name}' - {node.sclass}")
        for meth in node.methods:
            self.dot.edge(name, self.visit(meth))
        return name

    def visit(self, node : FuncDeclaration):
        name = self.name()
        self.dot.node(name,
            label=fr"FuncDeclaration\nname:'{node.name}'\nparameters: {node.parameters}",
            color=self.color)
        self.dot.edge(name, self.visit(node.stmts))
        return name

    def visit(self, node : VarDeclaration):
        name = self.name()
        self.dot.node(name,
            label=fr"VarDeclaration\nname={node.name}",
            color=self.color)
        if node.expr:
            self.dot.edge(name, self.visit(node.expr), label='init')
        return name

    # Statement

    def visit(self, node : Program):
        name = self.name()
        self.dot.node(name, label="Program", color=self.color)
        for d in node.decl:
            self.dot.edge(name, self.visit(d))
        return name

    def visit(self, node : Print):
        name = self.name()
        self.dot.node(name,
            label='Print',
            color=self.color)
        self.dot.edge(name, self.visit(node.expr))
        return name

    def visit(self, node : IfStmt):
        name = self.name()
        self.dot.node(name,
            label='IfStmt',
            color=self.color)
        self.dot.edge(name, self.visit(node.cond), label='test')
        if node.cons:
            self.dot.edge(name, self.visit(node.cons), label='then')
        if node.altr:
            self.dot.edge(name, self.visit(node.altr), label='else')
        return name

    def visit(self, node : WhileStmt):
        name = self.name()
        self.dot.node(name,
            label='WhileStmt',
            color=self.color)
        self.dot.edge(name, self.visit(node.cond), label='test')
        self.dot.edge(name, self.visit(node.body), label='body')
        return name

    def visit(self, node : ForStmt):
        name = self.name()
        self.dot.node(name,
            label='ForStmt',
            color=self.color)
        self.dot.edge(name, self.visit(node.for_init), label='init')
        self.dot.edge(name, self.visit(node.for_cond), label='cond')
        self.dot.edge(name, self.visit(node.for_increment), label='increment')
        self.dot.edge(name, self.visit(node.for_body), label='body')
        return name

    def visit(self, node : Return):
        name = self.name()
        self.dot.node(name,
            label='Return',
            color=self.color)
        if node.expr:
            self.dot.edge(name, self.visit(node.expr))
        return name

    def visit(self, node : ExprStmt):
        name = self.name()
        self.dot.node(name,
            label='ExprStmt',
            color=self.color)
        self.dot.edge(name, self.visit(node.expr))
        return name

    def visit(self, node : Expr):
        name  = self.name()
        label = 'Expr'
        if not self.program:
            self.program = True
        self.dot.node(name,
            label=label,
            color=self.color)
        for stmt in node.stmts:
            self.dot.edge(name, self.visit(stmt))
        return name

    # Expression

    def visit(self, node : Literal):
        name = self.name()
        value = node.value
        if node.value is None:
            value = "null"
        elif node.value is True:
            value = "true"
        elif node.value is False:
            value = "false"
        self.dot.node(name, label=fr"Literal\nvalue= {value}")
        return name

    def visit(self, node : Binary):
        name = self.name()
        self.dot.node(name, label=f"Binary '{node.op}'")
        self.dot.edge(name, self.visit(node.left))
        self.dot.edge(name, self.visit(node.right))
        return name

    def visit(self, node : Logical):
        name = self.name()
        self.dot.node(name, label=f"Logical '{node.op}'")
        self.dot.edge(name, self.visit(node.left))
        self.dot.edge(name, self.visit(node.right))
        return name

    def visit(self, node: Unary):
        name = self.name()
        self.dot.node(name, label=f'Unary {node.op}')
        self.dot.edge(name, self.visit(node.expr))
        return name

    def visit(self, node : Grouping):
        name = self.name()
        self.dot.node(name, label='Grouping')
        self.dot.edge(name, self.visit(node.expr))
        return name

    def visit(self, node : Variable):
        name = self.name()
        self.dot.node(name, label=f"Variable {node.name}")
        return name

    def visit(self, node : Assign):
        name = self.name()
        label = "Assign" if node.op == '=' else node.op
        self.dot.node(name, label=fr"{label}\nname: '{node.name}'")
        self.dot.edge(name, self.visit(node.expr))
        return name

    def visit(self, node : AssignPostfix):
        name = self.name()
        label = node.op
        self.dot.node(name, label=fr"{label}\n Postfix")
        self.dot.edge(name, self.visit(node.expr))
        return name

    def visit(self, node : AssignPrefix):
        name = self.name()
        label = node.op
        self.dot.node(name, label=fr"{label}\n Prefix")
        self.dot.edge(name, self.visit(node.expr))
        return name

    def visit(self, node : Call):
        name = self.name()
        self.dot.node(name, label=f"Call ")
        self.dot.edge(name, self.visit(node.func))
        if node.args is not None:
            for arg in node.args:
                self.dot.edge(name, self.visit(arg))
        return name

    def visit(self, node : Get):
        name = self.name()
        self.dot.node(name, label='')

        f'(get {self.visit(node.obj)} {node.name})'
        return name

    def visit(self, node : Set):
        name = self.name()
        self.dot.node(name, label='')
        f'(set {self.visit(node.obj)} {node.name} {self.visit(node.expr)})'
        return name

    def visit(self, node : This):
        name = self.name()
        self.dot.node(name, label='this ')
        return name

    def visit(self, node : Super):
        name = self.name()
        self.dot.node(name, label=f'super {node.name}')
        return name

    def visit(self, node : Continue):
        name = self.name()
        self.dot.node(name, label=f'continue')
        return name

    def visit(self, node : Break):
        name = self.name()
        self.dot.node(name, label=f'break')
        return name

    def visit(self, node : List):
        name = self.name()
        self.dot.node(name, label=f'list {node.name}')
        return name

