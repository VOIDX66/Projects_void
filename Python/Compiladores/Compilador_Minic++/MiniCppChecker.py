# checker.py
'''
Analisis Semantico
------------------

En esta etapa del compilador debemos hacer lo siguiente:

1. Construir la tabla de Símbolos (puede usar ChainMap).
2. Validar que todo Identificador debe ser declarado previamente.
3. Agregar una instrucción de cast.
4. Validar que cualquier expresión debe tener compatibilidad de tipos.
5. Validar que exista una función main (puerta de entrada).
6. Implementar la función scanf.
7. Implementar la instrucción FOR.
8. Validar que las instrucciones BREAK y CONTINUE estén utilizada dentro de instrucciones WHILE/FOR.
'''
from collections import ChainMap  # Tabla de Simbolos
from typing      import Union
from MiniCppCaster       import *

class CheckError(Exception):
  pass


def _check_name(name, env:ChainMap):
  for n, e in enumerate(env.maps):
    if name in e:
      if not e[name]:
        raise CheckError("No se puede hacer referencia a una variable en su propia inicialización")
      else:
        return n
  raise CheckError(f"'{name}' no esta definido")


class Checker(Visitor):

  @classmethod
  def check(cls, n:Node, env:ChainMap, interp):
    checker = cls()
    n.accept(checker, env.new_child())
    return checker

  # Declarations

  def visit(self, n:Program, env:ChainMap):
    '''
    1. Crear una nueva tabla de simbolos
    2. Insertar dentro de esa tabla funciones como: scanf, printf
    3. Visitar todas las declaraciones
    '''
    env = ChainMap()
    env['scanf'] = True
    env['prinf'] = True

    for decl in n.decls:
      decl.accept(self, env)

  def visit(self, n:FuncDeclStmt, env:ChainMap):
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
      env[p] = len(env)
    n.stmts.accept(self, env)

  def visit(self, n:VarDeclStmt, env:ChainMap, interp):
    '''
    1. Agregar n.ident a la TS actual
    '''
    env[n.ident] = n

  # Statements

  def visit(self, n:CompoundStmt, env: ChainMap, interp):
    '''
    1. Crear una tabla de simbolos
    2. Visitar Declaration/Statement
    '''
    newenv = env.new_child()
    for decl in n.decls:
      decl.accept(self, newenv, interp)
    for stmt in n.stmts:
      stmt.accept(self, newenv, interp)

  def visit(self, n:IfStmt, env:ChainMap, interp):

    '''
    1. Visitar n.expr (validar tipos)
    2. Visitar Stament por n.then
    3. Si existe opcion n.else_, visitar
    '''
    n.expr.accept(self, env, interp)
    n.then.accept(self, env, interp)
    if n.else_:
      n.else_.accept(self, env, interp)

  def visit(self, n:WhileStmt, env:ChainMap, interp):
    '''
    1. Visitar n.expr (validar tipos)
    2. visitar n.stmt
    '''
    env['while'] = True
    n.expr.accept(self, env, interp)
    n.stmt.accept(self, env, interp)
    env['while'] = False

  def visit(self, n:Union[BreakStmt, ContinueStmt], env: ChainMap, interp):
    '''
    1. Verificar que esta dentro de un ciclo while
    '''
    name = 'break' if isinstance(n, BreakStmt) else 'continue'
    if 'while' not in env:
      interp.ctxt.error(n, f'{name} usado fuera de un while/for')

  def visit(self, n:ReturnStmt, env:ChainMap, interp):
    '''
    1. Si se ha definido n.expr, validar que sea del mismo tipo de la función
    '''
    if n.expr:
      n.expr.accept(self, env, interp)
      if 'fun' not in env:
        interp.ctxt.error(n, 'return usado fuera de una funcion')

  def visit(self, node: ExprStmt, env: ChainMap, interp):
    node.expr.accept(self, env, interp)

  # Expressions

  def visit(self, n:ConstExpr, env:ChainMap, interp):
    pass

  def visit(self, n: BinaryOpExpr, env:ChainMap, interp):
    '''
    1. visitar n.left y luego n.right
    2. Verificar compatibilidad de tipos
    '''
    n.left.accept(self, env, interp)
    n.right.accept(self, env, interp)

  def visit(self, n:UnaryOpExpr, env:ChainMap, interp):
    '''
    1. visitar n.expr
    2. validar si es un operador unario valido
    '''
    n.expr.accept(self, env, interp)

  def visit(self, n:VarExpr, env:ChainMap, interp):
    '''
    1. Verificar si n.ident existe en TS y obtener el tipo
    '''
    try:
      interp.localmap[id(n)] = _check_name(n.name, env)
    except CheckError as err:
      interp.ctxt.error(n, str(err))

  def visit(self, n:VarAssignmentExpr, env:ChainMap, interp):
    '''
    1. Validar n.ident
    2. Visitar n.expr
    3. Verificar si son tipos compatibles
    '''
    n.expr.accept(self, env, interp)
    try:
      interp.localmap[id(n)] = _check_name(n.name, env)
    except CheckError as err:
      interp.ctxt.error(n, str(err))

  def visit(self, n:CallExpr, env:ChainMap, interp):
    '''
    1. Validar si n.ident existe
    2. visitar n.args (si estan definicos)
    3. verificar que len(n.args) == len(fun.params)
    4. verificar que cada arg sea compatible con cada param de la función
    '''
    n.func.accept(self, env, interp)
    for arg in n.args:
      arg.accept(self, env, interp)