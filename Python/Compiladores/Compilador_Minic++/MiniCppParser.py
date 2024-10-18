from rich import print
from MiniCppLexer import Lexer
from MiniCppCaster import *
import sly

class Parser(sly.Parser):
    debugfile = 'minicc.txt'
    tokens = Lexer.tokens

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
        return p.decl_list + [p.decl]

    @_("decl")
    def decl_list(self, p):
        return [p.decl]

    @_("var_decl", "func_decl", "class_decl")
    def decl(self, p):
        return p[0]

    @_("type_spec IDENT '=' expr ';'")
    def var_decl(self, p):
        return VarDeclStmt(p.type_spec, p.IDENT, p.expr)

    @_("type_spec IDENT ';'")
    def var_decl(self, p):
        return VarDeclStmt(p.type_spec, p.IDENT)
    
    @_("type_spec IDENT '[' expr ']' ';'")
    def var_decl(self, p):
        return VarDeclStmt(p.type_spec, p.IDENT, size = p.expr)

    @_("VOID", "BOOL", "INT", "FLOAT", "DOUBLE", "CHAR")
    def type_spec(self, p):
        return p[0]

    @_("type_spec IDENT '(' params ')' compound_stmt")
    def func_decl(self, p):
        return FuncDeclStmt(p.type_spec, p.IDENT, p.params, p.compound_stmt)

    @_("param_list", "VOID")
    def params(self, p):
        return p.param_list if hasattr(p, 'param_list') else []

    @_("param { ',' param }")
    def param_list(self, p):
        return [p.param0] + p.param1

    @_("type_spec IDENT")
    def param(self, p):
        return VarDeclStmt(p.type_spec, p.IDENT)

    @_("type_spec IDENT '[' ']'")
    def param(self, p):
        return VarDeclStmt(p.type_spec, p.IDENT)

    @_("'{' local_decls stmt_list '}'")
    def compound_stmt(self, p):
        return p.local_decls + p.stmt_list

    @_("local_decl local_decls")
    def local_decls(self, p):
        return [p.local_decl] + p.local_decls

    @_("empty")
    def local_decls(self, p):
        return []

    @_("var_decl")
    def local_decl(self, p):
        return p.var_decl

    @_("stmt stmt_list")
    def stmt_list(self, p):
        return [p.stmt] + p.stmt_list

    @_("empty")
    def stmt_list(self, p):
        return []

    @_("expr_stmt", "compound_stmt", "if_stmt", "while_stmt", "return_stmt", "break_stmt")
    def stmt(self, p):
        return p[0]

    @_("CLASS IDENT '{' var_decl_list '}'")
    def class_decl(self, p):
        return ClassDecl(p.IDENT, p.var_decl_list)
    
    @_("var_decl_list var_decl")
    def var_decl_list(self, p):
        return p.var_decl_list + [p.var_decl]

    @_("var_decl")
    def var_decl_list(self, p):
        return [p.var_decl]

    @_("expr ';'")
    def expr_stmt(self, p):
        return ExprStmt(p.expr)

    @_("';'")
    def expr_stmt(self, p):
        return ExprStmt()
    
    @_("PRINTF '(' expr ',' args ')' ';'")
    def expr_stmt(self, p):
        return CallExpr("printf", [p.expr] + p.args)
    
    @_("SCANF '(' expr ',' args ')' ';'")
    def expr_stmt(self, p):
        return CallExpr("scanf", [p.expr] + p.args)

    @_("WHILE '(' expr ')' stmt")
    def while_stmt(self, p):
        return WhileStmt(p.expr, p.stmt)

    @_("IF '(' expr ')' stmt ELSE stmt")
    def if_stmt(self, p):
        return IfStmt(p.expr, p.stmt0, p.stmt1)

    @_("IF '(' expr ')' stmt %prec IF")
    def if_stmt(self, p):
        return IfStmt(p.expr, p.stmt)

    @_("RETURN expr ';'")
    def return_stmt(self, p):
        return ReturnStmt(expr = p.expr)

    #@_("RETURN ';'")
    #def return_stmt(self, p):
    #    return ReturnStmt()

    @_("BREAK ';'", "CONTINUE ';'")
    def break_stmt(self, p):
        return BreakStmt() if p[0] == 'BREAK' else ContinueStmt()

    @_("IDENT '=' expr")
    def expr(self, p):
        return VarAssignmentExpr(p.IDENT, p.expr)

    @_("IDENT '[' expr ']' '=' expr")
    def expr(self, p):
        return ArrayAssignmentExpr(p.IDENT, p.expr0, p.expr1)

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
        return BinaryOpExpr(p[1], p[0], p[2])

    @_("'!' expr", "'-' expr %prec UNARY", "'+' expr %prec UNARY")
    def expr(self, p):
        return UnaryOpExpr(p[0], p[1])

    @_("'(' expr ')'")
    def expr(self, p):
        return p[1]

    @_("IDENT")
    def expr(self, p):
        return VarExpr(p[0])

    @_("IDENT '[' expr ']'")
    def expr(self, p):
        return ArrayAccessExpr(p[0], p[2])

    @_("IDENT '(' args ')'")
    def expr(self, p):
        return CallExpr(p[0], p[2])

    @_("IDENT '.' SIZE")
    def expr(self, p):
        return ArraySizeExpr(p[0], p[2])

    @_("BOOL_LIT", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "CHAR_LIT")
    def expr(self, p):
        return LiteralExpr(p[0])

    @_("NEW type_spec '[' expr ']'")
    def expr(self, p):
        return NewArrayExpr(p.type_spec, p[2])

    @_("arg_list", "empty")
    def args(self, p):
        return p.arg_list if hasattr(p, 'arg_list') else []

    @_("expr")
    def arg_list(self, p):
        return [p.expr]
    
    @_("arg_list ',' expr")
    def arg_list(self, p):
        return p.arg_list + [p.expr]
    
    @_("")
    def empty(self, p):
        pass

    def error(self, p):
        if p:
            print(f"Línea {p.lineno} error de sintaxis en '{p.value}' ({p.type})")
            self.errok()
        else:
            print("error de sintaxis en EOF")

def parse(source):
    lex = Lexer()  # Crea una instancia del lexer
    pas = Parser()  # Crea una instancia del parser
    
    # Analiza el código fuente y devuelve el nodo raíz del AST
    ast_root = pas.parse(lex.tokenize(source))
    
    return ast_root  # Devuelve el AST generado

def gen_ast(data,name):
    ast = parse(data)
    dot_visitor = MakeDot()
    ast.accept(dot_visitor)
    #Guardamos en formato png
    dot_visitor.dot.render(filename=f'{name}_ast', format='png', cleanup=True)
    return None,ast 

if __name__ == '__main__':
    data = open("isqrt.mcc", encoding='utf-8').read()
    gen_ast(data)

