from MiniCppCast import *
from MiniCppBuiltins import *

class Symtab:
    class SymbolDefinedError(Exception):
        pass

    def __init__(self, parent=None):
        self.entries = {}
        for k,v in stdlibFunctions.items():
            self.entries[k]=v
        self.parent = parent
        if self.parent:
            self.parent.children.append(self)
        self.children = []

    def add(self, name, value):
        if name in self.entries:
            raise Symtab.SymbolDefinedError()
        self.entries[name] = value

    def get(self, name):
        if name in self.entries:
            return self.entries[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            return None


InLoop=False
class Checker(Visitor):
    def _add_symbol(self, node, env: Symtab):
        try:
            env.add(node.name, node)
        except Symtab.SymbolDefinedError:
            self.error(node, f"Checker error, this symbol '{node.name}' is already defined.")

    def error(cls, position, txt):
        cls.ctxt.error(position, txt)

    @classmethod
    def check(cls, model, ctxt):
        cls.ctxt = ctxt
        check = cls()
        model.accept(check)
        return check

    def visit(self, node: Node):
        s1=Symtab()
        self.visit(node, s1)

    def visit(self, node: ClassDeclaration, env: Symtab):
        self._add_symbol(node, env)
        if node.sclass:
            value = env.get(node.sclass)
            if value is None:
                self.error(node, f"Checker error, parent class not found: '{node.sclass}'")
        #env = Symtab(env)
        for meth in node.methods:
            self.visit(meth, env)

    def visit(self, node: FuncDeclaration, env: Symtab):
        self._add_symbol(node, env)

        env = Symtab(env)

        if node.parameters:
            for param in node.parameters:
                self._add_symbol(Variable(param), env)
        self.visit(node.stmts, env)

    def visit(self, node: VarDeclaration, env: Symtab):
        self._add_symbol(node, env)
        if node.expr:
            self.visit(node.expr, env)

    # Statement
    def visit(self, node: Program, env: Symtab):
        #self._add_symbol(node, env)
        for d in node.decl:
            self.visit(d, env)

    def visit(self, node: Expr, env: Symtab):
        env = Symtab(env)
        for stmt in node.stmts:
            self.visit(stmt, env)

    def visit(self, node: Print, env: Symtab):
        self.visit(node.expr, env)

    def visit(self, node: IfStmt, env: Symtab):
        self.visit(node.cond, env)
        self.visit(node.cons, env)
        if node.altr:
            self.visit(node.altr, env)

    def visit(self, node: WhileStmt, env: Symtab):
        global InLoop
        self.visit(node.cond, env)
        InLoop=True
        self.visit(node.body, env)
        InLoop=False

    def visit(self, node: ForStmt, env: Symtab):
        global InLoop
        env = Symtab(env)
        self.visit(node.for_init, env)
        self.visit(node.for_cond, env)
        self.visit(node.for_increment, env)
        InLoop=True
        self.visit(node.for_body, env)
        InLoop=False

    def visit(self, node: Return, env: Symtab):
        '''
        1. Visitar expresion
        '''
        if node.expr:
            self.visit(node.expr, env)

    def visit(self, node: Continue, env: Symtab):
        if not InLoop:
            self.error(node, f"Checker error, '{node.name}' not in a loop")

    def visit(self, node: Break, env: Symtab):
        if not InLoop:
            self.error(node, f"Checker error, '{node.name}' not in a loop")

    def visit(self, node: ExprStmt, env: Symtab):
        if node.expr is not None:
            self.visit(node.expr, env)

    # Expression

    def visit(self, node: Literal, env: Symtab):
        pass

    def visit(self, node: Binary, env: Symtab):
        self.visit(node.left, env)
        self.visit(node.right, env)

    def visit(self, node: Logical, env: Symtab):

        self.visit(node.left, env)
        self.visit(node.right, env)

    def visit(self, node: Unary, env: Symtab):
        self.visit(node.expr, env)

    def visit(self, node: Grouping, env: Symtab):
        self.visit(node.expr, env)

    def visit(self, node: Variable, env: Symtab):
        result = env.get(node.name)
        if result is None:
            self.error(node, f"Checker error, the variable '{node.name}' is not defined")

    def visit(self, node: Assign, env: Symtab):
        result = env.get(node.name)
        if result is None:
            self.error(node, f"Checker error. Assign left symbol '{node.name}' is not defined")

        self.visit(node.expr, env)

    def visit(self, node: AssignPostfix, env: Symtab):
        self.visit(node.expr, env)

    def visit(self, node: AssignPrefix, env: Symtab):
        self.visit(node.expr, env)

    def visit(self, node: Call, env: Symtab):
        self.visit(node.func, env)
        result = env.get(node.func.name)
        if node.args is not None:
            for arg in node.args:
                self.visit(arg, env)

        if result is FuncDeclaration:
            if result is not None:
                if result.parameters is not None:
                    if len(result.parameters)!=len(node.args):
                        self.error(node, "Checker error, given arguments don't match expected arguments in Call")

    def visit(self, node: Get, env: Symtab):
        self.visit(node.obj, env)
        nam = env.get(node.name)
        if nam is None:
            self.error(node, f"Checker error. Get symbol '{node.name}' is not defined")

    def visit(self, node: Set, env: Symtab):
        self.visit(node.obj, env)
        nam= env.get(node.name)

        if nam is None:
            self.error(node, f"Checker Error. Set symbol '{node.name}' is not defined")

    def visit(self, node: This, env: Symtab):
        pass

    def visit(self, node: Super, env: Symtab):
        pass
