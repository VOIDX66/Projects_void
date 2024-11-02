# mcontext.py
'''
Clase de nivel superior que contiene todo sobre el 
analisis/ejecucion de un programa en Mini-C++

Sirve como repositorio de información sobre el programa,
inluido el codigo fuente, informe de errores, etc.
'''
from rich     import print
from collections import ChainMap
from MiniCppCaster    import Node
from MiniCppLexer    import Lexer
from MiniCppParser import Parser

class Context:
    def __init__(self):
        self.lexer  = Lexer()#Lexer(self)
        self.parser = Parser()#Parser(self)
        self.source = ''
        self.ast    = None
        self.have_errors = False
        self.env = ChainMap()

    def parse(self, source):
        self.have_errors = False
        self.source = source
        self.ast = self.parser.parse(self.lexer.tokenize(self.source))
        #print(f"AST: {self.ast}")
    
    def run(self):
        if not self.have_errors:
            pass
    
    def find_source(self, node):
        indices = self.parser.index_position(node)
        if indices:
            return self.source[indices[0]:indices[1]]
        else:
            return f"{type(node).__name__} (fuente no disponible)"
    
    def error(self, position, message):
        if isinstance(position, Node):
            lineno = self.parser.line_position(position)
            (start, end) = (part_start, part_end) = self.parser.index_position(position)
            while start >= 0 and self.source[start] != '\n':
                start -= 1

            start += 1
            while end < len(self.source) and self.source[end] != '\n':
                end += 1
            print()
            print(self.source[start:end])
            print(" "*(part_start - start), end='')
            print("^"*(part_end - part_start))
            print(f"{lineno}: {message}")
        else:
            print(f"{position}: {message}")
        self.have_errors = True