from collections import ChainMap  # Tabla de Símbolos
from typing import Union
from MiniCppCaster import *

class CheckError(Exception):
    pass

def _check_name(name, env: ChainMap):
    for e in env.maps:
        if name in e:
            if not e[name]:
                raise CheckError("No se puede hacer referencia a una variable en su propia inicialización")
            return
    raise CheckError(f"'{name}' no está definido")

class Checker(Visitor):

    @classmethod
    def check(cls, n: Node, env: ChainMap):
        checker = cls()
        ts = n.accept(checker, env)
        #print(ts.maps)
        return ts

    # Declarations
    #def visit(self, node, env):
    #    print(f"No hay un método visit definido para {type(node)}")
    #    raise NotImplementedError(f"No se puede visitar {type(node)}")

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
        
        return env  # Retornar el entorno

    def visit(self, n: FuncDeclStmt, env: ChainMap):
        '''
        1. Guardar la función en la TS
        2. Crear una TS para la función
        3. Agregar n.params dentro de la TS
        4. Visitar n.stmts 
        '''
        #env[n.ident] = type(n), newenv = env.new_child()
        newenv = env.new_child()
        newenv['fun'] = True
        for p in n.params:
            newenv[p.ident] = len(newenv)
        env[n.ident] = (type(n), newenv)
        n.compound_stmt.accept(self, newenv)

        # Retornar el entorno actualizado
        print(f"COSO HIJO: \n”{newenv}\n")
        return newenv  

    def visit(self, n: VarDeclStmt, env: ChainMap):
        '''
        1. Agregar n.ident a la TS actual
        '''
        if n.ident in env:
            raise CheckError(f"La variable '{n.ident}' ya ha sido declarada.")
        env[n.ident] = type(n)

        # Retornar el entorno actualizado
        return env  

    # Statements
    def visit(self, n: CompoundStmt, env: ChainMap):
        '''
        1. Crear una tabla de simbolos
        2. Visitar Declaration/Statement
        '''
        newenv = env.new_child()
        for stmt in n.stmts:
            stmt.accept(self, newenv)

        # Retornar el nuevo entorno
        return newenv  

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

        return env  # Retornar el entorno

    def visit(self, n: WhileStmt, env: ChainMap):
        '''
        1. Visitar n.expr (validar tipos)
        2. visitar n.then (es un stmt)
        '''
        env['while'] = True
        n.expr.accept(self, env)
        for body_stmt in n.then:  # Asumiendo que stmt.then es una lista de declaraciones
            body_stmt.accept(self, env)
        del env['while']

        return env  # Retornar el entorno

    def visit(self, n: Union[BreakStmt, ContinueStmt], env: ChainMap):
        '''
        1. Verificar que esta dentro de un ciclo while
        '''
        if 'while' not in env and 'for' not in env:
            raise CheckError(f"{'break' if isinstance(n, BreakStmt) else 'continue'} usado fuera de un ciclo")

        return env  # Retornar el entorno

    def visit(self, n: ReturnStmt, env: ChainMap):
        '''
        1. Si se ha definido n.expr, validar que sea del mismo tipo de la función
        '''
        if n.expr:
            n.expr.accept(self, env)
        if 'fun' not in env:
            raise CheckError("return usado fuera de una función")

        return env  # Retornar el entorno

    def visit(self, node: ExprStmt, env: ChainMap):
        node.expr.accept(self, env)
        return env  # Retornar el entorno

    # Expressions
    def visit(self, n: ConstExpr, env: ChainMap):
        return env  # Retornar el entorno

    def visit(self, n: BinaryOpExpr, env: ChainMap):
        '''
        1. visitar n.left y luego n.right
        2. Verificar compatibilidad de tipos
        '''
        n.left.accept(self, env)
        n.right.accept(self, env)

        return env  # Retornar el entorno

    def visit(self, n: UnaryOpExpr, env: ChainMap):
        '''
        1. visitar n.expr
        2. validar si es un operador unario valido
        '''
        n.expr.accept(self, env)

        return env  # Retornar el entorno

    def visit(self, n: VarExpr, env: ChainMap):
        '''
        1. Verificar si n.ident existe en TS y obtener el tipo
        '''
        _check_name(n.ident, env)
        return env  # Retornar el entorno

    def visit(self, n: VarAssignmentExpr, env: ChainMap):
        '''
        1. Validar n.ident
        2. Visitar n.expr
        3. Verificar si son tipos compatibles
        '''
        _check_name(n.var.ident, env)
        n.expr.accept(self, env)

        return env  # Retornar el entorno

    def visit(self, n: CallExpr, env: ChainMap):
        '''
        1. Validar si n.ident existe
        2. visitar n.args (si están definidos)
        3. verificar que len(n.args) == len(fun.params)
        4. verificar que cada arg sea compatible con cada param de la función
        '''
        for arg in n.args:
            arg.accept(self, env)

        return env  # Retornar el entorno

    def visit(self, node: LiteralExpr, env: ChainMap):
        # Guardar el valor del literal en el entorno
        value = node.value
        
        # Aquí se podría usar una clave que identifique el literal.
        env['literal_value'] = value
        
        return env  # Retornar el entorno
