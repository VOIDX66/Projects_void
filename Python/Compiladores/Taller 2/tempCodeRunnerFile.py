# coding: utf-8
from rich import print
import sly


class Lexer(sly.Lexer):
    tokens = {
        # keywords
        LET, READ, DATA, PRINT, GOTO, IF,
        THEN, FOR, NEXT, TO, STEP, END,
        STOP, DEF, GOSUB, DIM, REM, RETURN,
        RUN, LIST, NEW,

        # operadores de relacion
        LT, LE, GT, GE, NE, 

        # identificador
        ID,

        # constantes
        INTEGER, NUMBER, STRING,
    }
    literals = '+-*/^()=:,;'

    # ignorar 
    ignore = r' \t\r'   

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # expresiones regulares
    @_(r'REM.*\n')
    def REM(self, t):
        self.lineno += 1
        return t

    LET    = r'LET' 
    READ   = r'READ'
    DATA   = r'DATA'
    PRINT  = r'PRINT'
    GOTO   = r'GO ?TO'
    IF     = r'IF'
    THEN   = r'THEN'
    FOR    = r'FOR'
    NEXT   = r'NEXT'
    TO     = r'TO'
    STEP   = r'STEP'
    END    = r'END'
    STOP   = r'STOP'
    DEF    = r'DEF'
    GOSUB  = r'GOSUB'
    DIM    = r'DIM'
    RETURN = r'RETURN'

    ID = r'[A-Z][0-9]?'

    LE = r'<='
    GE = r'>='
    NE = r'<>'
    LT = r'<'
    GT = r'>'

    INTEGER = r'\d+'
    NUMBER  = r'(?:\d+(?:\.\d*)?|\.\d+)'
    STRING  = r'"[^"]*"?'

    def error(self, t):
        print(f"Línea [yello]{t.lineno}[/yello]: [red]caracter ilegal '{t.value[0]}'[/red]")
        self.index += 1

def pprint(source):
    from rich.table import Table
    from rich.console import Console

    lex = Lexer()

    table = Table(title='Análisis Léxico')
    table.add_column('type')
    table.add_column('value')
    table.add_column('lineno', justify='right')

    for tok in lex.tokenize(source):
        value = tok.value if isinstance(tok.value, str) else str(tok.value)
        table.add_row(tok.type, value, str(tok.lineno))

    console = Console()
    console.print(table)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('[red]usage: baslex.py filename[/red]')
        sys.exit(1)

    pprint(open(sys.argv[1], encoding='utf-8').read())