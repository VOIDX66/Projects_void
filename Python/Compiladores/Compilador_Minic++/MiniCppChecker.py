from collections import ChainMap  # Tabla de Símbolos
from typing import Union
from MiniCppCaster import *
from MiniCppTypeSys import *

class CheckError(Exception):
    pass

def _check_name(name, env: ChainMap):
    for e in env.maps:
        if name in e:
            if not e[name]:
                raise CheckError("No se puede hacer referencia a una variable en su propia inicialización")
            return
    raise CheckError(f"'{name}' no está definido")

#Lista para guardar los distintos ChainMaps
mapas = []

class Checker(Visitor):
    
    @classmethod
    def check(cls, n: Node, env: ChainMap):
        checker = cls()
        mapas.append(n.accept(checker, env))
        return mapas

    # Declarations
    def visit(self, n: Program, env: ChainMap):
        env = ChainMap({'scanf': True, 'printf': True})
        main_defined = False

        # Visitar los declaraciones y verificar que la función main se haya definido
        for stmt in n.stmts:
            if isinstance(stmt, FuncDeclStmt) and stmt.ident == "main":
                main_defined = True
            stmt.accept(self, env)

        if not main_defined:
            raise CheckError("No se ha definido la función 'main'")

        return env  # Retornar el entorno global

    def visit(self, n: FuncDeclStmt, env: ChainMap):
        # Guardar la función en la TS
        env[n.ident] = type(n)
        fun_env = env.new_child()  # Crear tabla de símbolos para la función
        fun_env['fun'] = True # Guardamos que es un ChainMap de una funcion
        fun_env['fun_name'] = n.ident

        # Agregar parámetros a la tabla de símbolos de la función
        for p in n.params:
            fun_env[p.ident] = type(p)  # Agregar parámetros a la tabla de símbolos de la función
        mapas.append(n.compound_stmt.accept(self, fun_env))  # Visitar el cuerpo de la función
        return fun_env  # Retornar el entorno de la función
        

    def visit(self, n: VarDeclStmt, env: ChainMap):
        if n.ident in env:
            raise CheckError(f"La variable '{n.ident}' ya ha sido declarada.")
        
        # Guardamos en el ChainMap con su respectivo tipo de clase y tipo de la función int, float, bool, etc...
        env[n.ident] = (type(n),n.type_spec)
        # Si le asignamos valor a la función
        if n.expr:
            expre = n.expr.accept(self, env)
            # Solo verificamos compatibilidad de tipos cuando tenemos los valores literales
            if isinstance(n.expr, LiteralExpr):
                #Verificar compatibilidad de tipos
                if env[n.ident][1] != type(expre).__name__:
                    raise CheckError(f"Tipos incompatibles en la declaración de '{n.ident}'")
            #casos unarios
            if isinstance(n.expr, UnaryOpExpr):
                if isinstance(n.expr.expr , LiteralExpr):
                    if env[n.ident][1] != type(n.expr.expr.accept(self,env)).__name__:
                        raise CheckError(f"Tipos incompatibles en la declaración de '{n.ident}'")

    # Statements
    def visit(self, n: CompoundStmt, env: ChainMap):
        comp_env = env.new_child()  # Crear una nueva tabla de símbolos
        for stmt in n.stmts:
            stmt.accept(self, comp_env)  # Visitar cada declaración/statement
        return comp_env

    def visit(self, n: IfStmt, env: ChainMap):
        n.expr.accept(self, env)  # Validar expresión
        n.then.accept(self, env)  # Validamos los statements del then
        if n.else_: # Si tenemos un else validamos los statements del else
            n.else_.accept(self, env)
        return env  # Retornar el entorno

    def visit(self, n: WhileStmt, env: ChainMap):
        env['while'] = True  # Indicar que estamos dentro de un ciclo
        n.expr.accept(self, env)  # Validar expresión
        n.then.accept(self, env)
        del env['while']  # Limpiar el entorno
        return env  # Retornar el entorno

    def visit(self, n: ForStmt, env: ChainMap):
        env['for'] = True  # Indicar que estamos dentro de un ciclo for

        if n.init:  # Validar la expresión de inicialización, si existe
            n.init.accept(self, env)
        
        if n.cond:  # Validar la condición, si existe
            n.cond.accept(self, env)
        
        if n.update:  # Validar la actualización, si existe
            n.update.accept(self, env)
        
        n.then.accept(self, env)

        del env['for']  # Limpiar el entorno
        return env  # Retornar el entorno actualizado


    def visit(self, n: Union[BreakStmt, ContinueStmt], env: ChainMap):
        # Validamos si las intrucciones break y continue estan dentro de un ciclo While / For
        if 'while' not in env and 'for' not in env:
            raise CheckError(f"{'break' if isinstance(n, BreakStmt) else 'continue'} usado fuera de un ciclo")
        return env  # Retornar el entorno

    def visit(self, n: ReturnStmt, env: ChainMap):
        if n.expr:
            n.expr.accept(self, env)  # Validar expresión
        if 'fun' not in env:
            raise CheckError("return usado fuera de una función")
        return env  # Retornar el entorno

    def visit(self, n: ExprStmt, env: ChainMap):
        n.expr.accept(self, env)  # Validar expresión
        return env  # Retornar el entorno

    # Expressions
    def visit(self, n: ConstExpr, env: ChainMap):
        return env  # Retornar el entorno

    def visit(self, n: BinaryOpExpr, env: ChainMap):
        left = n.left.accept(self, env)  # Visitar lado izquierdo
        right = n.right.accept(self, env)  # Visitar lado derecho
        
        if isinstance(n.left, LiteralExpr) and isinstance(n.right, LiteralExpr):
            result = check_binary_op(n.opr, type(left).__name__, type(right).__name__)
            if not result:
                raise CheckError(f"Operación no soportada: {left} {n.opr} {right}")
        return env  # Retornar el entorno

    def visit(self, n: UnaryOpExpr, env: ChainMap):
        una = n.expr.accept(self, env)  # Visitar expresión
        result = check_unary_op(n.opr, type(una).__name__)
        if not result:
            raise CheckError(f"Operación no soportada: {n.opr} {una}")
        return env  # Retornar el entorno

    def visit(self, n: VarExpr, env: ChainMap):
        _check_name(n.ident, env)  # Verificar si la variable existe
        return env[n.ident]  # Retornar el tipo de la variable

    def visit(self, n: VarAssignmentExpr, env: ChainMap):
        _check_name(n.var.ident, env)  # Validar variable
        expre = n.expr.accept(self, env)  # Visitar expresión
        # Verificar compatibilidad de tipos
        if isinstance(n.expr, LiteralExpr):
            if env[n.var.ident][1] != type(expre).__name__:
                raise CheckError(f"Tipos incompatibles en la asignación de '{n.var.ident}'")
        #casos unarios
        if isinstance(n.expr, UnaryOpExpr):
            if isinstance(n.expr.expr , LiteralExpr):
                if env[n.var.ident][1] != type(n.expr.expr.accept(self,env)).__name__:
                    raise CheckError(f"Tipos incompatibles en la declaración de '{n.var.ident}'")
        return env  # Retornar el entorno

    def visit(self, n: CallExpr, env: ChainMap):
        if n.ident not in env:
            raise CheckError(f"'{n.ident}' no está definido")
        else:
          for arg in n.args:
              arg.accept(self, env)  # Visitar argumentos
          return env  # Retornar el entorno

    def visit(self, n: LiteralExpr, env: ChainMap):
        return n.value  # Retornar el valor del literal
    
    def visit(self, n: CastExpr, env: ChainMap):
        # Obtener el tipo de la expresión original
        source_type = n.expr.accept(self, env)
        if isinstance(source_type, tuple):
            result_type = check_cast(n.type_spec, source_type[1])
            if result_type is None:
                raise CheckError(f"No se puede realizar el cast de {source_type[1]} a {n.type_spec}")
        if isinstance(n.expr, UnaryOpExpr):
            if isinstance(n.expr.expr, LiteralExpr):
                result_type = check_cast(n.type_spec, type(n.expr.expr.value).__name__)
                if result_type is None:
                    raise CheckError(f"No se puede realizar el cast de {type(n.expr.expr.value).__name__} a {n.type_spec}")
                # Retornar el tipo de destino si el cast es válido
        return env
