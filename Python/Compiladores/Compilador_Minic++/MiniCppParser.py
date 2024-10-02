#https://sly.readthedocs.io/en/latest/sly.html
#https://en.cppreference.com/w/cpp/language/operator_precedence

'''
Analizador Sintactico (LALR)
'''
from rich import print
from MiniCppLexer import Lexer
from MiniCppCaster import *
import sly

class Parser(sly.Parser):
    debugfile = 'minicc.txt'

    tokens = Lexer.tokens

    # Definir las Reglas de la gramática

    precedence = (
        ('nonassoc', IF),
        ('nonassoc', ELSE),
        ('right', '='),
        ('left', OR),
        ('left', AND),
        ('left', EQ, NE),
        ('left', '<', LE, '>', GE),
        ('left', '+', '-'),
        ('left', '*', '/', '%'),
        ('right', UNARY, '!'),

    )

    @_("decl_list")
    def program(self, p):
        return Program(p.decl_list)

    @_("decl_list decl")
    def decl_list(self, p):
        return p.decl_list + [ p.decl ]

    @_("decl")
    def decl_list(self, p):
        return [ p.decl ]

    @_("var_decl", "func_decl", "class_decl")
    def decl(self, p):
        '''
        decl ::= var_decl | func_decl | class_decl
        '''
        return p[0]

    # Inicializar variable
    @_("type_spec IDENT ';'")
    def var_decl(self, p):
        '''
        var_decl ::=  type_spec IDENT ';'
        '''
        return VarDeclStmt(p.type_spec, p.IDENT)

    # Declarar variable normal
    @_("var_decl IDENT '=' expr ';'")
    def var_decl(self, p):
        '''
        var_decl ::= type_spec IDENT '=' expr ';'
        '''
        return VarDeclStmt(p.type_spec, p.IDENT, p.expr)

    # Inicializar un array
    @_("type_spec IDENT '[' ']' ';'")
    def var_decl(self, p):
        '''
        var_decl ::=  type_spec IDENT '[' ']' ';'
        '''
        # Este nodo representa la declaración de un arreglo sin tamaño
        #return VarDeclStmt(p.type_spec, p.IDENT, is_array=True)
        return VarDeclStmt(p.type_spec, p.IDENT)

    # Inicializar array con un tamaño en específico
    @_("type_spec IDENT '[' expr ']' ';'")
    def var_decl(self, p):
        '''
        var_decl ::= type_spec IDENT '[' expr ']' ';'
        '''
        # Este nodo representa la declaración de un arreglo con tamaño
        #return VarDeclStmt(p.type_spec, p.IDENT, is_array=True, size=p.expr)
        return VarDeclStmt(p.type_spec, p.IDENT, size=p.expr)

    @_("VOID", "BOOL", "INT", "FLOAT")
    def type_spec(self, p):
        '''
        type_spec ::= VOID | BOOL | INT | FLOAT
        '''
        return p[0]

    @_("type_spec IDENT '(' params ')' compound_stmt")
    def func_decl(self, p):
        '''
        func_decl ::= type_spec IDENT '(' params ')' compound_stmt
        '''
        return FuncDeclStmt(p.type_spec, p.IDENT, p.params, p.compound_stmt)

    @_("param_list", "VOID")
    def params(self, p):
        '''
        params ::= param_list | VOID
        '''
        return p.param_list if hasattr(p, 'param_list') else []

    @_("param { ',' param }")
    def param_list(self, p):
        '''
        param_list ::= param ( ',' param )*
        '''
        return [p.param0] + p.param1

    @_("type_spec IDENT")
    def param(self, p):
        '''
        param ::= type_spec IDENT
        '''
        # Nodo que representa un parámetro de función
        return VarDeclStmt(p.type_spec, p.IDENT)

    @_("type_spec IDENT '[' ']'")
    def param(self, p):
        '''
        param ::= type_spec IDENT '[' ']'
        '''
        # Nodo que representa un parámetro de función que es un arreglo
        #return VarDeclStmt(p.type_spec, p.IDENT, is_array=True)
        return VarDeclStmt(p.type_spec, p.IDENT)

    @_("'{' local_decls stmt_list '}'")
    def compound_stmt(self, p):
        '''
        compound_stmt ::= '{' local_decls stmt_list '}'
        '''
        return p.local_decls + p.stmt_list

    @_("local_decl local_decls")
    def local_decls(self, p):
        return [p.local_decl] + p.local_decls

    @_("empty")
    def local_decls(self, p):
        return []

    @_("var_decl")
    def local_decl(self, p):
        '''
        local_decl ::= type_spec IDENT ';'
        '''
        return p.var_decl

    @_("stmt stmt_list")
    def stmt_list(self, p):
        return [p.stmt] + p.stmt_list

    @_("empty")
    def stmt_list(self, p):
        return []

    @_("expr_stmt", "compound_stmt", "if_stmt", "while_stmt", "return_stmt", "break_stmt")
    def stmt(self, p):
        '''
        stmt ::= expr_stmt | compound_stmt | if_stmt | while_stmt | return_stmt | break_stmt
        '''
        return p[0]

    @_("CLASS IDENT '{' var_decl_list '}'")
    def class_decl(self, p):
        '''
        class_decl ::= CLASS IDENT '{' var_decl_list '}'
        '''
        return ClassDecl(p.IDENT, p.var_decl_list)

    @_("var_decl_list var_decl")
    def var_decl_list(self, p):
        return p.var_decl_list + [p.var_decl]

    @_("var_decl")
    def var_decl_list(self, p):
        return [p.var_decl]


    @_("expr ';'")
    def expr_stmt(self, p):
        '''
        expr_stmt ::= expr ';'
        '''

    @_("';'")
    def expr_stmt(self, p):
        '''
        expr_stmt ::= ';'
        '''

    @_("WHILE '(' expr ')' stmt")
    def while_stmt(self, p):
        '''
        while_stmt ::= WHILE '(' expr ')' stmt
        '''

    @_("IF '(' expr ')' stmt")
    def if_stmt(self, p):
        return IfStmt(p.expr, p.stmt)

    @_("IF '(' expr ')' stmt ELSE stmt ",
       "IF '(' expr ')' stmt %prec IF")
    def if_stmt(self, p):
        return IfStmt(p.expr, p.stmt0, p.stmt1)

    @_("RETURN expr ';'")
    def return_stmt(self, p):
        return ReturnStmt(p.expr)

    @_("RETURN ';'")
    def return_stmt(self, p):
        return ReturnStmt()

    @_("BREAK ';'", "CONTINUE ';'")
    def break_stmt(self, p):
        '''
        break_stmt ::= ( BREAK | CONTINUE ) ';'
        '''

    @_("IDENT '=' expr")
    def expr(self, p):
        '''
        expr ::= IDENT '=' expr
        '''

    @_("IDENT '[' expr ']' '=' expr")
    def expr(self, p):
        '''
        expr ::= IDENT '[' expr ']' '=' expr
        '''

    @_("expr OR expr",
       "expr AND expr",
       "expr EQ expr",
       "expr NE expr",
       "expr LE expr",
       "expr '<' expr",
       "expr GE expr",
       "expr '>' expr",
       "expr '+' expr",
       "expr '-' expr",
       "expr '*' expr",
       "expr '/' expr",
       "expr '%' expr")
    def expr(self, p):
        '''
        expr ::=  expr 'OR' expr
            | expr 'AND' expr
            | expr 'EQ' expr | expr 'NE' expr
            | expr 'LE' expr | expr '<' expr | expr 'GE' expr | expr '>' expr
            | expr '+' expr | expr '-' expr
            | expr '*' expr | expr '/' expr | expr '%' expr
        '''

    @_("'!' expr", "'-' expr %prec UNARY", "'+' expr %prec UNARY")
    def expr(self, p):
        '''
        expr ::= '!' expr | '-' expr | '+' expr
        '''

    @_("'(' expr ')'")
    def expr(self, p):
        '''
        expr ::= '(' expr ')'
        '''

    @_("IDENT")
    def expr(self, p):
        '''
        expr ::= IDENT
        '''

    @_("IDENT '[' expr ']'")
    def expr(self, p):
        '''
        expr ::= IDENT '[' expr ']'
        '''

    @_("IDENT '(' args ')'")
    def expr(self, p):
        '''
        expr ::= IDENT '(' args ')'
        '''

    @_("IDENT '.' SIZE")
    def expr(self, p):
        '''
        expr ::= IDENT '.' SIZE
        '''

    @_("BOOL_LIT", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "CHAR_LIT")
    def expr(self, p):
        '''
        expr ::= BOOL_LIT | INT_LIT | FLOAT_LIT | STRING_LIT | CHAR_LIT
        '''

    @_("NEW type_spec '[' expr ']'")
    def expr(self, p):
        '''
        expr ::= NEW type_spec '[' expr ']'
        '''

    @_("arg_list", "empty")
    def args(self, p):
        '''
        args ::= arg_list |
        ''' 

    @_("expr [ ',' expr ]")
    def arg_list(self, p):
        '''
        arg_list ::= expr ( ',' expr )*
        '''

    @_("")
    def empty(self, p):
        pass

    def error(self, p):
        if p:
            print(f"Línea {p.lineno} error de sintaxis en '{p.value}' ({p.type})")
            # Just discard the token and tell the parser it's okay.
            self.errok()
        else:
            print("error de sintaxis en EOF")

def parse(source):
    lex = Lexer()
    pas = Parser()

    pas.parse(lex.tokenize(source))

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print(f"[red]Usage mclex.py textfile[/red]")
        exit(1)

    parse(open(sys.argv[1], encoding='utf-8').read())
