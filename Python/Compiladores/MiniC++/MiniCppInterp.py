# cinterp.py
'''
Tree-walking interpreter
'''
from collections import ChainMap
from MiniCppCast    import *
from MiniCppChecker import Checker
from rich    import print
from MiniCppBuiltins import *

import math

# Veracidad en MiniC
def _is_truthy(value):
	if isinstance(value, bool):
		return value
	elif value is None: 
		return False
	else:
		return True 

class ReturnException(Exception):
	def __init__(self, value):
		self.value = value

class MiniCExit(BaseException):
	pass

class AttributeError(Exception):
	pass

class Function:
	def __init__(self, node, env):
		self.node = node
		self.env = env

	def __call__(self, interp, *args): 
		if self.node.parameters is not None:
			if len(args) != len(self.node.parameters):
				raise CallError(f"Interp Error. Expected {len(self.node.parameters)} arguments")
		newenv = self.env.new_child() 
		if self.node.parameters is not None:
			for name, arg in zip(self.node.parameters, args):
				newenv[name] = arg

		oldenv = interp.env 
		interp.env = newenv
		try:
			interp.visit(self.node.stmts)
			result = None
		except ReturnException as e:
			result = e.value
		finally:
			interp.env = oldenv 
		return result

	def bind(self, instance): 
		env = self.env.new_child() 
		env['this'] = instance 
		return Function(self.node, env)


class Class:
	def __init__(self, name, sclass, methods):
		self.name = name
		self.sclass = sclass
		self.methods = methods

	def __str__(self): 
		return self.name

	def __call__(self, *args): 
		this = Instance(self)
		init = self.find_method('init')
		if init:
			init.bind(this)(*args) 
		return this

	def find_method(self, name):
		meth = self.methods.get(name)
		if meth is None and self.sclass:
			return self.sclass.find_method(name)
		return meth

class Instance:
	def __init__(self, klass):
		self.klass = klass
		self.data = { }

	def __str__(self):
		return self.klass.name + " instance"

	def get(self, name):
		if name in self.data:
			return self.data[name]
		method = self.klass.find_method(name)
		if not method:
			raise AttributeError(f'interp Error, Not defined property {name}')
		return method.bind(self)

	def set(self, name, value):
		self.data[name] = value

ThereIsBreak=False
ThereIsContinue=False

class Interpreter(Visitor): 
	def __init__(self, ctxt):
		self.ctxt = ctxt 	
		self.env  = ChainMap()		

	def _check_numeric_operands(self, node, left, right):
		if isinstance(left, (int, float)) and isinstance(right, (int, float)):
			return True
		else:
			self.error(node, f"Interp Error. In '{node.op}' the operands must be numerical type")

	def _check_numeric_operand(self, node, value):
		if isinstance(value, (int, float)):
			return True
		else:
			self.error(node, f"Interp Error. In '{node.op}' the operand must be numerical type")

	def error(self, position, message):
		self.ctxt.error(position, message)
		raise MiniCExit()

	def interpret(self, node):
		try:
			Checker.check(node, self.ctxt)
			if not self.ctxt.have_errors:
				self.visit(node)
			else:
				print("\n The interpreter could not start because the Checker returned errors")
		except MiniCExit as e:
			pass

	def visit(self, node: Expr):
		for stmt in node.stmts:
			self.visit(stmt)
			if ThereIsBreak:
				return 0
			if ThereIsContinue:
				return 1

	def visit(self, node: Program):
		for k,v in stdlibFunctions.items():
			self.env[k]=v
		for d in node.decl:
			self.visit(d)

	def visit(self, node: ClassDeclaration):
		if node.sclass:
			sclass = self.visit(node.sclass)
			env = self.env.new_child()
			env['super'] = sclass			
		else:
			sclass = None
			env = self.env
		methods = { }
		for meth in node.methods:
			methods[meth.name] = Function(meth, env)
		cls = Class(node.name, sclass, methods)
		self.env[node.name] = cls

	def visit(self, node: FuncDeclaration):

		func = Function(node, self.env)
		self.env[node.name] = func

	def visit(self, node: VarDeclaration):
		if node.expr:
			expr = self.visit(node.expr)
		else:
			expr = None
		self.env[node.name] = expr

	def visit(self, node: Print):
		print(self.visit(node.expr))

	def visit(self, node: WhileStmt):
		global ThereIsContinue
		global ThereIsBreak

		while _is_truthy(self.visit(node.cond)):
			ThereIsContinue = False
			ThereIsBreak = False
			flowControl = self.visit(node.body)
			if flowControl == 0:
				break
			elif flowControl == 1:
				continue
			else:
				pass

	def visit(self, node: Continue):
		global ThereIsContinue
		ThereIsContinue = True

	def visit(self, node: Break):
		global ThereIsBreak
		ThereIsBreak = True

	def visit(self, node: ForStmt):
		global ThereIsContinue
		global ThereIsBreak

		self.visit(node.for_init)
		while _is_truthy(self.visit(node.for_cond)):
			ThereIsContinue = False
			ThereIsBreak = False
			flowControl = self.visit(node.for_body)
			if flowControl == 0:
				break
			elif flowControl == 1:
				continue
			else:
				pass
			self.visit(node.for_increment)

	def visit(self, node: IfStmt):
		test = self.visit(node.cond)
		if _is_truthy(test):
			self.visit(node.cons)
		elif node.altr:
			self.visit(node.altr)

	def visit(self, node: Return):
		raise ReturnException(self.visit(node.expr))

	def visit(self, node: ExprStmt):
		self.visit(node.expr)

	def visit(self, node: Literal):
		return node.value

	def visit(self, node: Binary):
		left  = self.visit(node.left)
		right = self.visit(node.right)
		if node.op == '+':
			(isinstance(left, str) and isinstance(right, str)) or self._check_numeric_operands(node, left, right)
			return left + right
		elif node.op == '-':
			self._check_numeric_operands(node, left, right)
			return left - right
		elif node.op == '*':
			self._check_numeric_operands(node, left, right)
			return left * right
		elif node.op == '/':
			self._check_numeric_operands(node, left, right)
			return left / right
		elif node.op == '%':
			self._check_numeric_operands(node, left, right)
			return left % right
		elif node.op == '==':
			return left == right
		elif node.op == '!=':
			return left != right
		elif node.op == '<':
			self._check_numeric_operands(node, left, right)
			return left < right
		elif node.op == '>':
			self._check_numeric_operands(node, left, right)
			return left > right
		elif node.op == '<=':
			self._check_numeric_operands(node, left, right)
			return left <= right
		elif node.op == '>=':
			self._check_numeric_operands(node, left, right)
			return left >= right
		else:
			raise NotImplementedError(f"Interp Error. Wrong Operator {node.op}")

	def visit(self, node: Logical):
		left = self.visit(node.left)
		if node.op == '||':
			return left if _is_truthy(left) else self.visit(node.right)
		if node.op == '&&':
			return self.visit(node.right) if _is_truthy(left) else left
		raise NotImplementedError(f"Interp Error. Wrong Operator {node.op}")

	def visit(self, node: Unary):
		expr = self.visit(node.expr)
		if node.op == "-":
			self._check_numeric_operand(node, expr)
			return - expr
		elif node.op == "!":
			return not _is_truthy(expr)
		else:
			raise NotImplementedError(f"Interp Error. Wrong Operator {node.op}")

	def visit(self, node: Grouping):
		return self.visit(node.expr)

	def visit(self, node: Assign):
		expr = 0
		if node.op == "=":
			expr = self.visit(node.expr)
		elif node.op == "+=":
			expr = self.env[node.name] + self.visit(node.expr)
		elif node.op == "-=":
			expr = self.env[node.name] - self.visit(node.expr)
		elif node.op == "*=":
			expr = self.env[node.name] * self.visit(node.expr)
		elif node.op == "/=":
			expr = self.env[node.name] / self.visit(node.expr)
		elif node.op == "%=":
			expr = self.env[node.name] % self.visit(node.expr)
		self.env[node.name] = expr

	def visit(self, node: AssignPostfix):
		temp = self.visit(node.expr)
		expr=0
		if node.op == "++":
			expr = self.visit(node.expr) + 1
		else:
			expr = self.visit(node.expr) - 1
		self.env[node.expr.name]=expr
		return temp

	def visit(self, node: AssignPrefix):
		expr = 0
		if node.op == "++":
			expr = self.visit(node.expr) + 1
		else:
			expr = self.visit(node.expr) - 1
		self.env[node.expr.name]=expr
		return expr

	def visit(self, node: Call):
		callee = self.visit(node.func)
		if not callable(callee):
			self.error(node.func, f'Interp Error {self.ctxt.find_source(node.func)!r} is not callable')

		if node.args is not None:
			args = [ self.visit(arg) for arg in node.args ]
		else:
			args = []
		try:
			return callee(self, *args)
		except CallError as err:
			self.error(node.func, str(err))

	def visit(self, node: Variable):
		return self.env[node.name]

	def visit(self, node: Set):
		obj = self.visit(node.obj)
		val = self.visit(node.expr)
		if isinstance(obj, Instance):
			obj.set(node.name, val)
			return val
		else:
			self.error(node.obj, f'Interp Error{self.ctxt.find_source(node.obj)!r} is not an instance')

	def visit(self, node: Get):
		obj = self.visit(node.obj)
		if isinstance(obj, Instance):
			try:
				return obj.get(node.name)
			except AttributeError as err:
				self.error(node.obj, str(err))
		else:
			self.error(node.obj, f'Interp Error{self.ctxt.find_source(node.obj)!r}  is not an instance')

	def visit(self, node: This):
		return self.env['this']

	def visit(self, node: Super):
		distance = self.localmap[id(node)]
		sclass = self.env.maps[distance]['super']
		this = self.env.maps[distance-1]['this']
		method = sclass.find_method(node.name)
		if not method:
			self.error(node.object, f'Interp Error. Not defined property {node.name!r}')
		return method.bind(this)
