import sly

class Lexer(sly.Lexer):
    def __init__(self, ctxt):
        self.ctxt=ctxt

    tokens = {
        # Palabras reservadas
        FUN, VAR, PRINT, IF, ELSE, WHILE, RETURN, TRUE, FALSE,
        CLASS, FOR, WHILE, TRUE, NULL, THIS, SUPER,

        PLUS, MINUS, TIMES, DIVIDE, POINT, SEMI, COMMA, LPAREN,
        RPAREN, LBRACE, RBRACE, LT, LE, GT, GE,
        EQ, NE, AND, OR, NOT, ASSIGN, MODULE, END_IF,

        # Otros tokens
        IDENT, NUM, REAL, STRING,

        ADDEQ, MINEQ, TIMESEQ, DIVIDEEQ, MODULEEQ,

        PLUSPLUS, MINUSMINUS, CONTINUE, BREAK
    }
    literals = '+-*/%=(){}[];,'

    # Ignoramos espacios en blanco (white-space)
    ignore = ' \t\r'

    # Ignoramos newline
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Ignorar Comentarios de varias líneas
    @_(r'/\*(.|\n)*\*/')
    def ignore_comments(self, t):
        self.lineno += t.value.count('\n')

    # Ignorar Comentarios de una sola línea
    @_(r'//.*\n')
    def ignore_cppcomments(self, t):
        self.lineno += 1

    # Definicion de Tokens a traves de regexp
    PLUSPLUS = r'\+\+'
    ADDEQ = r'\+='
    PLUS = r'\+'
    MINUSMINUS = r'--'
    MINEQ =  r'-='
    MINUS =r'-'
    TIMESEQ =  r'\*='
    TIMES =r'\*'
    DIVIDEEQ =  r'/='
    DIVIDE =r'/'
    POINT =r'\.'
    SEMI =r';'
    COMMA =r','
    LPAREN =r'\('
    RPAREN =r'\)'
    LBRACE =r'{'
    RBRACE =r'}'
    LE  = r'<='
    LT  = r'<'
    GE  = r'>='
    GT  = r'>'
    EQ  = r'=='
    NE  = r'!='
    AND = r'&&'
    OR  = r'\|\|'
    NOT = r'!'
    ASSIGN=r'='
    MODULEEQ =  r'%='
    MODULE=r'%'

    IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
    IDENT['fun']    = FUN
    IDENT['var']    = VAR
    IDENT['print']  = PRINT
    IDENT['if']     = IF
    IDENT['else']   = ELSE
    IDENT['while']  = WHILE
    IDENT['return'] = RETURN
    IDENT['true']   = TRUE
    IDENT['false']  = FALSE
    IDENT['class']  = CLASS
    IDENT['for']  = FOR
    IDENT['while']  = WHILE
    IDENT['null']  = NULL
    IDENT['this']  = THIS
    IDENT['super']  = SUPER
    IDENT['end_if'] = END_IF
    IDENT['continue'] = CONTINUE
    IDENT['break'] = BREAK

    @_(r'".*"')
    def STRING(self, t):
        t.value = str(t.value)
        return t

    @_(r'(\d+\.\d*)|(\.\d+)')
    def REAL(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def NUM(self, t):
        t.value = int(t.value)
        return t

    def error(self, t):
        self.ctxt.error(t, f"LEX ERROR. Illegal character {str(t.value[0])} + at line: {self.lineno}")
        self.index += 1
