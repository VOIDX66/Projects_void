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
	def check(cls, n, env:ChainMap, interp):
		checker = cls()
		n.accept(checker, env, interp)
		return checker

	# Declarations
			
	def visit(self, n:FuncDeclStmt, env:ChainMap, interp):
		env[n.ident] = True
		env = env.new_child()
		env['fun'] = True
		for p in n.params:
			env[p] = len(env)
		n.stmts.accept(self, env, interp)
		
	def visit(self, n:VarDeclStmt, env:ChainMap, interp):
		env[n.ident] = False
		if n.expr:
			n.expr.accept(self, env, interp)
		env[n.ident] = True

	# Statements
		
	def visit(self, n:IfStmt, env:ChainMap, interp):
		n.expr.accept(self, env, interp)
		n.then.accept(self, env, interp)
		if n.else_:
			n.else_.accept(self, env, interp)
			
	def visit(self, n:WhileStmt, env:ChainMap, interp):
		env['while'] = True
		n.expr.accept(self, env, interp)
		n.stmt.accept(self, env, interp)

	def visit(self, n:Union[BreakStmt, ContinueStmt], env: ChainMap, interp):
		name = 'break' if isinstance(n, BreakStmt) else 'continue'
		if 'while' not in env:
			interp.ctxt.error(n, f'{name} usado fuera de un while/for')

	def visit(self, n:ReturnStmt, env:ChainMap, interp):
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
		n.left.accept(self, env, interp)
		n.right.accept(self, env, interp)
		
	def visit(self, n:UnaryOpExpr, env:ChainMap, interp):
		n.expr.accept(self, env, interp)
				
	def visit(self, n:VarExpr, env:ChainMap, interp):
		try:
			interp.localmap[id(n)] = _check_name(n.name, env)
		except CheckError as err:
			interp.ctxt.error(n, str(err))
			
	def visit(self, n:VarAssignmentExpr, env:ChainMap, interp):
		n.expr.accept(self, env, interp)
		try:
			interp.localmap[id(n)] = _check_name(n.name, env)
		except CheckError as err:
			interp.ctxt.error(n, str(err))

	def visit(self, n:CallExpr, env:ChainMap, interp):
		n.func.accept(self, env, interp)
		for arg in n.args:
			arg.accept(self, env, interp)