
from MiniCppLexer import Lexer
import sly
from MiniCppCast import *

class Parser(sly.Parser):
    debugfile="minic.txt"
    tokens = Lexer.tokens

    def __init__(self, ctxt):
        self.ctxt=ctxt

    precedence = (
        ('left', PLUSPLUS),
        ('left', MINUSMINUS),
        ('right', ADDEQ),
        ('right', MINEQ),
        ('right', TIMESEQ),
        ('right', DIVIDEEQ),
        ('right', MODULEEQ),
        ('right', ASSIGN),    
        ('left', OR),
        ('left', AND),
        ('left', EQ, NE),
        ('left', LT, LE, GT, GE),
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE, MODULE),
        ('right', UNARY),
    )

    @_("{ declaration }")
    def program(self, p):
        return Program(p.declaration)

    @_("class_declaration",
       "func_declaration",
       "var_declaration",
       "statement")
    def declaration(self, p):
        return p[0]

    @_("CLASS IDENT [ LPAREN LT IDENT RPAREN ] LBRACE { function } RBRACE ")
    def class_declaration(self, p):
        return ClassDeclaration(p.IDENT0, p.IDENT1, p.function)

    @_("FUN function")
    def func_declaration(self, p):
        return p[1]

    @_("VAR IDENT [ ASSIGN expression ] SEMI")
    def var_declaration(self, p):
        return VarDeclaration(p.IDENT, p.expression)

    @_("expr_stmt",
       "for_stmt",
       "if_stmt",
       "print_stmt",
       "return_stmt",
       "while_stmt",
       "block",
       "continue_stmt",
       "break_stmt")
    def statement(self, p):
        return p[0]

    @_("expression SEMI")
    def expr_stmt(self, p):
        return ExprStmt(p.expression)

    @_("FOR LPAREN for_initialize [ expression ] SEMI [ expression ] RPAREN statement")
    def for_stmt(self, p):
        return ForStmt(p.for_initialize,p.expression0,p.expression1,p.statement)

    @_("FOR LPAREN SEMI [ expression ] SEMI [ expression ] RPAREN statement")
    def for_stmt(self, p):
        return ForStmt(None,p.expression0,p.expression1,p.statement)

    @_("var_declaration",
        "expr_stmt")
    def for_initialize(self, p):
        return p[0]

    @_("CONTINUE SEMI")
    def continue_stmt(self, p):
        return Continue(p[0])

    @_("BREAK SEMI")
    def break_stmt(self, p):
        return Break(p[0])
    
    @_("IF LPAREN [ expression ] RPAREN statement [ ELSE statement ] END_IF")
    def if_stmt(self, p):
        return IfStmt(p.expression, p.statement0, p.statement1)

    @_("PRINT LPAREN expression RPAREN SEMI")
    def print_stmt(self, p):
        return Print(p.expression)

    @_("RETURN [ expression ] SEMI")
    def return_stmt (self, p):
        return Return(p.expression)

    @_("WHILE LPAREN expression RPAREN statement")
    def while_stmt(self, p):
        return WhileStmt(p.expression, p.statement)

    @_("LBRACE { declaration } RBRACE")
    def block(self, p):
        return Expr(p.declaration)

    @_("expression ASSIGN expression",
       "expression ADDEQ expression",
       "expression MINEQ expression",
       "expression TIMESEQ expression",
       "expression DIVIDEEQ expression",
       "expression MODULEEQ expression")
    def expression(self, p):
        if isinstance(p.expression0, Variable):
            return Assign(p[1], p.expression0.name, p.expression1)
        elif isinstance(p.expression0, Get):
            return Set(p.expression0.obj, p.expression0.name, p.expression1)
        else:
            raise SyntaxError(f"{p.lineno}: PARSER ERROR, it was impossible to assign {p.expression0}")

    @_("expression OR  expression",
       "expression AND expression")
    def expression(self, p):
        return Logical(p[1], p.expression0, p.expression1)

    @_("expression PLUS expression",
       "expression MINUS expression",
       "expression TIMES expression" ,
       "expression DIVIDE expression" ,
       "expression MODULE expression" ,
       "expression LT  expression" ,
       "expression LE  expression" ,
       "expression GT  expression" ,
       "expression GE  expression" ,
       "expression EQ  expression" ,
       "expression NE  expression")
    def expression(self, p):
        return Binary(p[1], p.expression0, p.expression1)

    @_("factor")
    def expression(self, p):
        return p.factor

    @_("REAL", "NUM", "STRING")
    def factor(self, p):
        return Literal(p[0])

    @_("TRUE", "FALSE")
    def factor(self, p):
        return Literal(p[0] == 'true')

    @_("NULL")
    def factor(self, p):
        return Literal(None)

    @_("THIS")
    def factor(self, p):
        return This()

    @_("IDENT")
    def factor(self, p):
        return Variable(p.IDENT)

    @_("SUPER POINT IDENT")
    def factor(self, p):
        return Super(p.IDENT)

    @_("factor POINT IDENT")
    def factor(self, p):
        return Get(p.factor, p.IDENT)

    @_("factor LPAREN [ arguments ] RPAREN ")
    def factor(self, p):
        return Call(p.factor, p.arguments)

    @_(" LPAREN expression RPAREN ")
    def factor(self, p):
        return Grouping(p.expression)

    @_("MINUS factor %prec UNARY",
       "NOT factor %prec UNARY")
    def factor(self, p):
        return Unary(p[0], p.factor)

    @_("factor PLUSPLUS",
       "factor MINUSMINUS")
    def factor(self, p):
        return AssignPostfix(p[1], p.factor)

    @_("PLUSPLUS factor",
       "MINUSMINUS factor")
    def factor(self, p):
        return AssignPrefix(p[0], p.factor)

    @_("IDENT LPAREN [ parameters ] RPAREN block")
    def function(self, p):
        return FuncDeclaration(p.IDENT, p.parameters, p.block)

    @_("IDENT { COMMA IDENT }")
    def parameters(self, p):
        return [ p.IDENT0 ] + p.IDENT1

    @_("expression { COMMA expression }")
    def arguments(self, p):
        return [ p. expression0 ] + p.expression1

    def error(self, p):
        if p:
            self.ctxt.error(p, f"PARSER ERROR, Syntax error in the Token {p.type} due to: {p}")
        else:
            self.ctxt.error(p, f"PARSER ERROR, Syntax Error in EOF. Check braces, semicolons and END_IF ")

def parse(source):
    lex = Lexer(source)  
    pas = Parser(source)  
    
    ast_root = pas.parse(lex.tokenize(source))
    
    return ast_root  

def gen_ast(data,name):
    ast = parse(data)
    dot_visitor = MakeDot()
    ast.accept(dot_visitor)
    dot_visitor.dot.render(filename=f'{name}_ast', format='png', cleanup=True)
    return None,ast     