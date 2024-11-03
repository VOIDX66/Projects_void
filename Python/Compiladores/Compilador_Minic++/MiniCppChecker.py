from collections import ChainMap  # Tabla de Símbolos
from typing import Union
from MiniCppCaster import *

class CheckError(Exception):
    pass

def _check_name(name, env: ChainMap):
    for e in env.maps:
        print(type(name),name)
        if name in e:
            if not e[name]:
                raise CheckError("No se puede hacer referencia a una variable en su propia inicialización")
            return
    raise CheckError(f"'{name}' no está definido")

class Checker(Visitor):

    @classmethod
    def check(cls, n: Node, env: ChainMap):
        checker = cls()
        n.accept(checker, env)
        return checker

    # Declarations
    def visit(self, node, env):
        print(f"No hay un método visit definido para {type(node)}")
        raise NotImplementedError(f"No se puede visitar {type(node)}")

    def visit(self, n: Program, env: ChainMap):
        '''
        1. Crear una nueva tabla de simbolos
        2. Insertar dentro de esa tabla funciones como: scanf, printf
        3. Visitar todas las declaraciones
        '''
        env = ChainMap({'scanf': True, 'printf': True})  # Usar un dict para iniciar el contexto
        main_defined = False

        for stmt in n.stmts:
            if isinstance(stmt, FuncDeclStmt) and stmt.ident == "main":
                main_defined = True
            stmt.accept(self, env)

        if not main_defined:
            raise CheckError("No se ha definido la función 'main'")

    def visit(self, n: FuncDeclStmt, env: ChainMap):
        '''
        1. Guardar la función en la TS
        2. Crear una TS para la función
        3. Agregar n.params dentro de la TS
        4. Visitar n.stmts 
        '''
        env[n.ident] = n
        env = env.new_child()
        env['fun'] = True
        for p in n.params:
            env[p.ident] = len(env)
        n.compound_stmt.accept(self, env)

    def visit(self, n: VarDeclStmt, env: ChainMap):
        '''
        1. Agregar n.ident a la TS actual
        '''
        if n.ident in env:
            raise CheckError(f"La variable '{n.ident}' ya ha sido declarada.")
        env[n.ident] = True

    # Statements
    def visit(self, n: CompoundStmt, env: ChainMap):
        '''
        1. Crear una tabla de simbolos
        2. Visitar Declaration/Statement
        '''
        newenv = env.new_child()
        #for decl in n.decls:
        #    decl.accept(self, newenv)
        for stmt in n.stmts:
            stmt.accept(self, newenv)

    def visit(self, n: IfStmt, env: ChainMap):
        '''
        1. Visitar n.expr (validar tipos)
        2. Visitar Stament por n.then
        3. Si existe opcion n.else_, visitar
        '''
        n.expr.accept(self, env)
        n.then.accept(self, env)
        if n.else_:
            n.else_.accept(self, env)

    def visit(self, n: WhileStmt, env: ChainMap):
        '''
        1. Visitar n.expr (validar tipos)
        2. visitar n.then (es un stmt)
        '''
        env['while'] = True
        n.expr.accept(self, env)
        #n.then.accept(self, env)
        for body_stmt in n.then:  # Asumiendo que stmt.then es una lista de declaraciones
            body_stmt.accept(self, env)
        del env['while']

    def visit(self, n: Union[BreakStmt, ContinueStmt], env: ChainMap):
        '''
        1. Verificar que esta dentro de un ciclo while
        '''
        if 'while' not in env and 'for' not in env:
            raise CheckError(f"{'break' if isinstance(n, BreakStmt) else 'continue'} usado fuera de un ciclo")

    def visit(self, n: ReturnStmt, env: ChainMap):
        '''
        1. Si se ha definido n.expr, validar que sea del mismo tipo de la función
        '''
        if n.expr:
            n.expr.accept(self, env)
        if 'fun' not in env:
            raise CheckError("return usado fuera de una función")

    def visit(self, node: ExprStmt, env: ChainMap):
        node.expr.accept(self, env)

    # Expressions
    def visit(self, n: ConstExpr, env: ChainMap):
        pass

    def visit(self, n: BinaryOpExpr, env: ChainMap):
        '''
        1. visitar n.left y luego n.right
        2. Verificar compatibilidad de tipos
        '''
        n.left.accept(self, env)
        n.right.accept(self, env)

    def visit(self, n: UnaryOpExpr, env: ChainMap):
        '''
        1. visitar n.expr
        2. validar si es un operador unario valido
        '''
        n.expr.accept(self, env)

    def visit(self, n: VarExpr, env: ChainMap):
        '''
        1. Verificar si n.ident existe en TS y obtener el tipo
        '''
        _check_name(n.ident, env)

    def visit(self, n: VarAssignmentExpr, env: ChainMap):
        '''
        1. Validar n.ident
        2. Visitar n.expr
        3. Verificar si son tipos compatibles
        '''
        _check_name(n.var.ident, env)
        n.expr.accept(self, env)

    def visit(self, n: CallExpr, env: ChainMap):
        '''
        1. Validar si n.ident existe
        2. visitar n.args (si están definidos)
        3. verificar que len(n.args) == len(fun.params)
        4. verificar que cada arg sea compatible con cada param de la función
        '''
       # _check_name(n.func.name, env)
        for arg in n.args:
            arg.accept(self, env)

    def visit(self, node: LiteralExpr, env):
        # Guardar el valor del literal en el entorno
        value = node.value
        
        # Aquí se podría usar una clave que identifique el literal, 
        # en este caso simplemente lo guardamos con una clave genérica.
        # Puedes ajustar esto según cómo gestiones las claves en tu entorno.
        env['literal_value'] = value
        
        # También puedes imprimirlo para depuración
        #print(f"Stored literal value in env: {value}")

        return value  # Puedes seguir devolviendo el valor si es necesario


