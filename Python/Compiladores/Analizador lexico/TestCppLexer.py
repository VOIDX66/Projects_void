#Pruebas unitarias sobre el Lexer del MiniCpp

import unittest
from MiniCppLexer import Lexer

class TestMiniCppLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()
    
    #Pruebas
    def test_literals(self):
        tokens = list(self.lexer.tokenize("10 1.1 'C' true \"CADENA\""))
        token_types = [token.type for token in tokens]
        self.assertEqual(token_types, ['INT_LIT', 'FLOAT_LIT', 'CHAR_LIT', 'BOOL_LIT', 'STRING_LIT'])

    def test_comments(self):
        tokens = list(self.lexer.tokenize("/********Comentario multilinea \\ #$%+-| //Texto *******/"))
        token_types = [token.type for token in tokens]
        self.assertEqual(token_types, [])#Ignora el comentario

    def test_comments_cpp(self):
        tokens = list(self.lexer.tokenize("//Comentario unica linea"))
        token_types = [token.type for token in tokens]
        self.assertEqual(token_types, [])#Ignora el comentario

    def test_operators(self):
        tokens = list(self.lexer.tokenize("&& || <= >= == !="))
        token_types = [token.type for token in tokens]
        self.assertEqual(token_types, ['AND', 'OR', 'LE', 'GE', 'EQ', 'NE'])

    def test_identifiers(self):
        tokens = list(self.lexer.tokenize("void bool int float char while if else continue break return size new class"))
        token_types = [token.type for token in tokens]
        self.assertEqual(token_types, [
                                        'VOID', 'BOOL', 'INT', 'FLOAT', 'CHAR', 'WHILE', 'IF', 'ELSE', 'CONTINUE', 'BREAK',
                                        'RETURN', 'SIZE', 'NEW', 'CLASS'
                                      ])
        
    def test_ilegal_characters(self):
        tokens = list(self.lexer.tokenize("$ + - ~ ¬ % \n \t"))
        token_types = [token.type for token in tokens]
        self.assertEqual(token_types, ['+', '-', '%'])


if __name__ == '__main__':
    unittest.main()