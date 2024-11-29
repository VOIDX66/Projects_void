import sly 
from rich import print

class Lexer(sly.Lexer):
    tokens = {
        #Palabras reservadas
        VOID, BOOL, INT, FLOAT, DOUBLE, CHAR, WHILE, FOR, IF, ELSE, CONTINUE, BREAK, RETURN, SIZE, NEW, CLASS, PRINTF, SPRINTF, SCANF,

        #Operadores de relacion
        AND, OR, EQ, NE, GE, LE,

        # Otros simbolos
        IDENT, BOOL_LIT, INT_LIT, FLOAT_LIT, STRING_LIT, CHAR_LIT
    }

    literals = '+-*/%=().,;[]{}<>!"'

    #ignorar saltos de linea
    @_(r'\n+')
    def ignore_lineno(self, t): #t abreviación de token, objeto que tiene 5 valores
        self.lineno += t.value.count('\n')

    #Ignorar patrones dentro del codigo fuente
    ignore = " \t"

    #Ignorar comentarios

    #ignore_cppcomment = r'//.*\n'
    @_(r'//.*')
    def ignore_cppcomment(self, t):
        self.lineno += 1

    #ignore_comment = r"/" #Buscar expresion regular para los comentarios multilinea
    @_(r'\/\*(\*(?!\/)|[^*])*\*\/')
    def ignore_comment(self, t):
        self.lineno += t.value.count('\n')
    
    @_(r'"(?:[^"\\]|\\.)*"')
    def STRING_LIT(self, t):
        # Extrae el valor de la cadena sin las comillas
        value = t.value[1:-1]  # Quita las comillas dobles
        # Maneja las secuencias de escape
        escape_sequences = {
            '\\"': '"',
            '\\\\': '\\',
            '\\n': '\n',
            '\\t': '\t'
        }
        # Reemplaza las secuencias de escape
        for escape, char in escape_sequences.items():
            value = value.replace(escape, char)
        t.value = value
        return t

    #Literales flotantes
    @_(r'\d+\.\d+')
    def FLOAT_LIT(self, t):
        t.value = float(t.value)
        return t

    #Literales enteros
    @_(r'\d+')
    def INT_LIT(self, t):
        t.value = int(t.value)
        return t
    
    #Literales booleanos
    @_(r'true|false')
    def BOOL_LIT(self, t):
        t.value = (t.value == 'true')
        return t

    @_(r"'(\\.|[^'\\])'")
    def CHAR_LIT(self, t):
        # Extrae el valor del carácter sin las comillas
        value = t.value[1:-1]
        # Maneja las secuencias de escape
        if value.startswith('\\'):
            # Para secuencias de escape como \n, \t, \'
            escape_sequences = {
                '\\n': '\n',
                '\\t': '\t',
                "\\'": "'",
                '\\\\': '\\'
            }
            value = escape_sequences.get(value, value)
        # Asigna el valor del carácter
        t.value = value
        return t
    
    #Caracteres ilegales
    def error(self, t):
        print(f"\nIllegal character {t.value[0]}")
        self.index += 1

    #Definicion de Tokens
    IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
    IDENT["void"] = VOID
    IDENT["bool"] = BOOL
    IDENT["int"] = INT
    IDENT["float"] = FLOAT
    IDENT["double"] = DOUBLE
    IDENT["char"] = CHAR
    IDENT["while"] = WHILE
    IDENT["for"] = FOR
    IDENT["if"] = IF
    IDENT["else"] = ELSE
    IDENT["continue"] = CONTINUE 
    IDENT["break"] = BREAK
    IDENT["return"] = RETURN
    IDENT["size"] = SIZE
    IDENT["new"] = NEW
    IDENT["class"] = CLASS
    IDENT["printf"] = PRINTF
    IDENT["format"] = SPRINTF
    IDENT["scanf"] = SCANF

    #Operadores
    EQ = r'=='
    NE = r'!='
    LE = r'<='
    GE = r'>='
    AND = r'&&'
    OR = r'\|\|'

def print_tokens():
    l = Lexer()
    d = '''void main(void) {
        /*Esto es un comentario  //Comentario dentro del comentario sigue*/
        printf("Hola mundo\n");
        string mensaje = format("Usuario: %s, Edad: %d, Saldo: %.2f", "Maria", 30, 1500.75);
        //Comentario
        /************************
        Este es otro comentario
        ************************/
        }'''
    
    for tok in l.tokenize(d):
        print(tok)

def print_lexer(data):
    l = Lexer()
    for tok in l.tokenize(data):
        print(tok)

if __name__ == '__main__':
    #data = open("isqrt.mcc", encoding='utf-8').read()
    #print_lexer(data)
    print_lexer('''void main(void) {
        /*Esto es un comentario  //Comentario dentro del comentario sigue*/
        printf("Hola mundo\n");
        string mensaje = format("Usuario: %s, Edad: %d, Saldo: %.2f", "Maria", 30, 1500.75);
        //Comentario
        /************************
        Este es otro comentario
        ************************/
        }''')