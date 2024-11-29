# context.py
from MiniCppLexer    import Lexer
from MiniCppParser  import Parser
from MiniCppInterp import Interpreter
from rich import print

import MiniCppCast

class Context:

	def __init__(self):
		self.lexer  = Lexer(self)
		self.parser = Parser(self)
		self.interp = Interpreter(self)
		self.source = ''
		self.ast    = None
		self.have_errors = False

	def parse(self, source): 
		self.have_errors = False
		self.source = source
		self.ast = self.parser.parse(self.lexer.tokenize(self.source))

	def run(self): 
		if not self.have_errors:
			return self.interp.interpret(self.ast)

	def find_source(self, node):
		indices = self.parser.index_position(node)
		if indices:
			return self.source[indices[0]:indices[1]]
		else:
			return f'{type(node).__name__} (Sorry, source not available)'

	def error(self, position, message):
		if isinstance(position, MiniCppCast.Node):
			lineno = self.parser.line_position(position)
			(start, end) = (part_start, part_end) = self.parser.index_position(position)
			while start >= 0 and self.source[start] != '\n':
				start -=1

			start += 1
			while end < len(self.source) and self.source[end] != '\n':
				end += 1
			print()
			print(self.source[start:end])
			print(" "*(part_start - start), end='')
			print("^"*(part_end - part_start))
			print(f'{lineno}: {message}')

		else:
			print(message)
		self.have_errors = True
