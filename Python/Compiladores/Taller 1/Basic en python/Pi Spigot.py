import re 
from collections import namedtuple, defaultdict, deque
import math
import random
import operator as op


program = '''
10   LET N = 1000
20   LET L1 = INT(10*N/3)
30   DIM A(L1)
40   FOR J = 1 TO l1
50      LET A(J) = 2
60   NEXT J
70   lET N9 = 0
80   LET P3 = 0
90   FOR J = 1 TO N
100     LET Q = 0
110     FOR I = L1 TO 1 STEP -1
120         LET X = 10*A(I)+Q*I
130         LET N2 = 2*I-1
140         LET A(I) = X-INT(X/N2)*N2
150         LET Q = INT(X/N2)
160     NEXT I
170     LET A(1) = Q-INT(Q/10)*10
180     LET Q = INT(Q/10)
190     IF Q=9 THEN 210
200      GOTO 230
210         LET N9 = N9+1
220         GOTO 390
230     IF Q=10 THEN 250
240     GOTO 310
250         FOR K = 1 TO N9
260             PRINT(0)
270         NEXT K
280         LET P3 = 0
290         LET N9 = 0
300         GO TO 390
310     PRINT(P3)
320     LET P3 = Q
330     IF N9 <> 0 THEN 350
340     GOTO 390
350         FOR K = 1 TO N9
360             PRINT(9)
370         NEXT K
380         LET N9 = 0
390  NEXT J
400  PRINT(P3)
410  REM COMENTARIO ACLARANDO NOMBRES L1 = LEN, N9 = NINES, P3 = PREDIGIT
420  END
'''
tokenize = re.compile(r'''
    \d* \.? \d+ (?: E -? \d+)?                     | # number 
    SIN|COS|TAN|ATN|EXP|ABS|LOG|SQR|RND|INT|FN[A-Z]| # functions
    LET|READ|DATA|PRINT|GOTO|IF|FOR|NEXT|END       | # keywords
    DEF|GOSUB|RETURN|DIM|REM|TO|THEN|STEP|STOP     | # keywords
    [A-Z]\d? | # variable names (letter + optional digit)
    ".*?"    | # labels (strings in double quotes)
    <>|>=|<= | # multi-character relational operators
    \S         # any non-space single character ''', 
    re.VERBOSE).findall

tokens = [] # Global variable to hold a list of tokens

def tokenizer(line):
    "Return a list of the tokens on this line, handling spaces properly, and upper-casing."
    line = ''.join(tokenize(line)) # Remove whitespace
    return tokenize(line.upper())

def peek(): 
    "Return the first token in the global `tokens`, or None if we are at the end of the line."
    return (tokens[0] if tokens else None)

def pop(constraint=None):
    """Remove and return the first token in `tokens`, or return None if token fails constraint.
    constraint can be None, a literal (e.g. pop('=')), or a predicate (e.g. pop(is_varname))."""
    top = peek()
    if constraint is None or (top == constraint) or (callable(constraint) and constraint(top)):
        return tokens.pop(0)
    
def remove_spaces(line): 
    "Remove white space from line, except space inside double quotes."
    return 

def lines(text): 
    "A list of the non-empty lines in a text."
    return [line for line in text.splitlines() if line]

def test_tokenizer():
    global tokens
    assert tokenizer('X-1') == ['X', '-', '1'] # Numbers don't have a leading minus sign, so this isn't ['X', '-1']
    assert tokenizer('PRINT "HELLO WORLD"') == ['PRINT', '"HELLO WORLD"']
    assert tokenizer('10 GOTO 99') == tokenizer('10GOTO99') == tokenizer('10 GO TO 99') == ['10', 'GOTO', '99']
    assert (tokenizer('100 PRINT "HELLO WORLD", SIN(X) ^ 2') == 
            ['100', 'PRINT', '"HELLO WORLD"', ',', 'SIN', '(', 'X', ')', '^', '2'])
    assert (tokenizer('100IFX1+123.4+E1-12.3E4 <> 1.2E-34*-12E34+1+"HI" THEN99') ==
            ['100', 'IF', 'X1', '+', '123.4', '+', 'E1', '-', '12.3E4', '<>', 
             '1.2E-34', '*', '-', '12E34', '+', '1', '+', '"HI"', 'THEN', '99'])
    assert lines('one line') == ['one line']
    assert lines(program) == [
     '10 REM POWER TABLE',
     '11 DATA 8, 4',
     '15 READ N0, P0',
     '20 PRINT "N",',
     '25 FOR P = 2 to P0',
     '30   PRINT "N ^" P,',
     '35 NEXT P',
     '40 PRINT "SUM"',
     '45 LET S = 0',
     '50 FOR N = 2 TO N0',
     '55   PRINT N,',
     '60   FOR P = 2 TO P0',
     '65     LET S = S + N ^ P',
     '70     PRINT N ^ P,',
     '75   NEXT P',
     '80   PRINT S',
     '85 NEXT N',
     '99 END']
    assert [tokenizer(line) for line in lines(program)] == [
     ['10', 'REM', 'P', 'O', 'W', 'E', 'R', 'T', 'A', 'B', 'L', 'E'],
     ['11', 'DATA', '8', ',', '4'],
     ['15', 'READ', 'N0', ',', 'P0'],
     ['20', 'PRINT', '"N"', ','],
     ['25', 'FOR', 'P', '=', '2', 'TO', 'P0'],
     ['30', 'PRINT', '"N ^"', 'P', ','],
     ['35', 'NEXT', 'P'],
     ['40', 'PRINT', '"SUM"'],
     ['45', 'LET', 'S', '=', '0'],
     ['50', 'FOR', 'N', '=', '2', 'TO', 'N0'],
     ['55', 'PRINT', 'N', ','],
     ['60', 'FOR', 'P', '=', '2', 'TO', 'P0'],
     ['65', 'LET', 'S', '=', 'S', '+', 'N', '^', 'P'],
     ['70', 'PRINT', 'N', '^', 'P', ','],
     ['75', 'NEXT', 'P'],
     ['80', 'PRINT', 'S'],
     ['85', 'NEXT', 'N'],
     ['99', 'END']]

    tokens = tokenizer('10 GO TO 99') 
    assert peek() == '10'
    assert pop()  == '10'
    assert peek() == 'GOTO'
    assert pop()  == 'GOTO'
    assert peek() == '99'
    assert pop(str.isalpha) == None    # '99' is not alphabetic
    assert pop('98.6') == None         # '99' is not '98.6'
    assert peek() == '99'
    assert pop(str.isnumeric)  == '99' # '99' is numeric
    assert peek() is None and not tokens 
    
    return 'ok'

def variable(): 
    "Parse a possibly subscripted variable e.g. 'X3' or 'A(I)' or 'M(2*I, 3)'."
    V = varname()
    if pop('('):
        indexes = list_of(expression)()
        pop(')') or fail('expected ")" to close subscript')
        return Subscript(V, indexes) # E.g. 'A(I)' => Subscript('A', ['I'])
    else: 
        return V                     # E.g. 'X3' 
    
def expression(prec=1): 
    "Parse an expression: a primary and any [op expression]* pairs with precedence(op) >= prec."
    exp = primary()                         # 'A' => 'A'
    while precedence(peek()) >= prec:
        op = pop()
        rhs = expression(precedence(op) + associativity(op))
        exp = Opcall(exp, op, rhs)          # 'A + B' => Opcall('A', '+', 'B')
    return exp

class list_of:
    "list_of(category) is a callable that parses a comma-separated list of <category>"
    def __init__(self, category): self.category = category
    def __call__(self):
        result = ([self.category()] if tokens else [])
        while pop(','):
            result.append(self.category())
        return result

def Grammar(): 
    return {
    'LET':    [variable, '=', expression],
    'READ':   [list_of(variable)],
    'DATA':   [list_of(number)],
    'PRINT':  [labels_and_expressions],
    'GOTO':   [linenumber],
    'IF':     [expression, relational, expression, 'THEN', linenumber],
    'FOR':    [varname, '=', expression, 'TO', expression, step],
    'NEXT':   [varname],
    'END':    [],
    'STOP':   [],
    'DEF':    [funcname, '(', varname, ')', '=', expression],
    'GOSUB':  [linenumber],
    'RETURN': [],
    'DIM':    [list_of(variable)], 
    'REM':    [anycharacters],
    'A':    []
    }

def statement():
    "Parse a BASIC statement from `tokens`."
    num  = linenumber()
    typ  = pop(is_stmt_type) or fail('unknown statement type')
    args = []
    for p in grammar[typ]: # For each part of rule, call if callable or match if literal string
        if callable(p):
            args.append(p())
        else:
            pop(p) or fail('expected ' + repr(p))
    return Stmt(num, typ, args)

def number():        return (-1 if pop('-') else +1) * float(pop()) # Optional minus sign
def step():          return (expression() if pop('STEP') else 1)    # 1 is the default step
def linenumber():    return (int(pop()) if peek().isnumeric() else fail('missing line number'))
def relational():    return pop(is_relational) or fail('expected a relational operator')
def varname():       return pop(is_varname)    or fail('expected a variable name')
def funcname():      return pop(is_funcname)   or fail('expected a function name')
def anycharacters(): tokens.clear() # Ignore tokens in a REM statement

def is_stmt_type(x):  return is_str(x) and x in grammar # LET, READ, ...
def is_funcname(x):   return is_str(x) and len(x) == 3 and x.isalpha()  # SIN, COS, FNA, FNB, ...
def is_varname(x):    return is_str(x) and len(x) in (1, 2) and x[0].isalpha() # A, A1, A2, B, ...
def is_label(x):      return is_str(x) and x.startswith('"') # "HELLO WORLD", ...
def is_relational(x): return is_str(x) and x in ('<', '=', '>', '<=', '<>', '>=')
def is_number(x):     return is_str(x) and x and x[0] in '.0123456789' # '3', '.14', ...

def is_str(x):        return isinstance(x, str)
    
def parse(program): return sorted(parse_line(line) for line in lines(program))

def parse_line(line): global tokens; tokens = tokenizer(line); return statement()

def parse_line(line):
    "Return a Stmt(linenumber, statement_type, arguments)."
    global tokens
    tokens = tokenizer(line)
    try:
        stmt = statement()
        if tokens: fail('extra tokens at end of line')
        return stmt
    except SyntaxError as err:
        print("Error in line '{}' at '{}': {}".format(line, ' '.join(tokens), err))
        return Stmt(0, 'REM', []) # Return dummy statement
        
def fail(message): raise SyntaxError(message)

Stmt      = namedtuple('Stmt',      'num, typ, args')     # '1 GOTO 9' => Stmt(1, 'GOTO', 9)
Subscript = namedtuple('Subscript', 'var, indexes')       # 'A(I)'     => Subscript('A', ['I'])
Funcall   = namedtuple('Funcall',   'f, x')               # 'SQR(X)'   => Funcall('SQR', 'X')
Opcall    = namedtuple('Opcall',    'x, op, y')           # 'X + 1'    => Opcall('X', '+', 1)
ForState  = namedtuple('ForState',  'continu, end, step') # Data for FOR loop 

class Function(namedtuple('_', 'parm, body')):
    "User-defined function; 'DEF FNC(X) = X ^ 3' => Function('X', Opcall('X', '^', 3))"
    def __call__(self, value):                           
        variables[self.parm] = value # Global assignment to the parameter
        return evalu(self.body)

def labels_and_expressions():
    "Parse a sequence of label / comma / semicolon / expression (for PRINT statement)."
    result = []
    while tokens:
        item = pop(is_label) or pop(',') or pop(';') or expression()
        result.append(item)
    return result


def primary():
    "Parse a primary expression (no infix op except maybe within parens)."
    if is_number(peek()):                   # '1.23' => 1.23 
        return number()
    elif is_varname(peek()):                # X or A(I) or M(I+1, J)
        return variable()
    elif is_funcname(peek()):               # SIN(X) => Funcall('SIN', 'X')
        return Funcall(pop(), primary())
    elif pop('-'):                          # '-X' => Funcall('NEG', 'X')
        return Funcall('NEG', primary())
    elif pop('('):                          # '(X)' => 'X'
        exp = expression()
        pop(')') or fail('expected ")" to end expression')
        return exp
    else:
        return fail('unknown expression')

def precedence(op): 
    return (3 if op == '^' else 2 if op in ('*', '/', '%') else 1 if op in ('+', '-') else 0)

def associativity(op): 
    return (0 if op == '^' else 1)

def test_exp(text, repr):
    "Test that text can be parsed as an expression to yield repr, with no tokens left over."
    global tokens
    tokens = tokenizer(text)
    return (expression() == repr) and not tokens
    
def test_parser():
    assert is_funcname('SIN') and is_funcname('FNZ') # Function names are three letters
    assert not is_funcname('X') and not is_funcname('')
    assert is_varname('X') and is_varname('A2') # Variables names are one letter and an optional digit
    assert not is_varname('FNZ') and not is_varname('A10') and not is_varname('')
    assert is_relational('>') and is_relational('>=') and not is_relational('+')
    
    assert test_exp('A + B * X + C', Opcall(Opcall('A', '+', Opcall('B', '*', 'X')), '+', 'C'))
    assert test_exp('A + B + X + C', Opcall(Opcall(Opcall('A', '+', 'B'), '+', 'X'), '+', 'C'))
    assert test_exp('SIN(X)^2',      Opcall(Funcall('SIN', 'X'), '^', 2))
    assert test_exp('10 ^ 2 ^ 3',    Opcall(10, '^', Opcall(2, '^', 3))) # right associative
    assert test_exp('10 - 2 - 3',    Opcall(Opcall(10, '-', 2), '-', 3)) # left associative
    assert test_exp('A(I)+M(I, J)',  Opcall(Subscript(var='A', indexes=['I']), '+', 
                                            Subscript(var='M', indexes=['I', 'J'])))
    assert test_exp('X * -1',        Opcall('X', '*', Funcall('NEG', 1.0)))
    assert test_exp('X--Y--Z',       Opcall(Opcall('X', '-', Funcall('NEG', 'Y')), 
                                            '-', Funcall('NEG', 'Z')))
    assert test_exp('((((X))))',     'X')
    return 'ok'

def run(program): execute(parse(program))

def execute(stmts): 
    "Parse and execute the BASIC program."
    global variables, functions, column
    functions, data = preprocess(stmts) # {name: function,...}, deque[number,...]
    variables = defaultdict(float) # mapping of {variable: value}, default 0.0
    column    = 0                  # column to PRINT in next
    pc        = 0                  # program counter
    ret       = 0                  # index (pc) that a GOSUB returns to
    fors      = {}                 # runtime map of {varname: ForState(...)}
    goto      = {stmt.num: i       # map of {linenumber: index}
                 for (i, stmt) in enumerate(stmts)}
    while pc < len(stmts):
        (_, typ, args) = stmts[pc] # Fetch and decode the instruction
        pc += 1                    # Increment the program counter
        if typ in ('END', 'STOP') or (typ == 'READ' and not data): 
            return
        elif typ == 'LET':
            V, exp = args
            let(V, evalu(exp))
        elif typ == 'READ':
            for V in args[0]:
                let(V, data.popleft())
        elif typ == 'PRINT':
            basic_print(args[0])
        elif typ == 'GOTO':
            pc = goto[args[0]]
        elif typ == 'IF':
            lhs, relational, rhs, dest = args
            if functions[relational](evalu(lhs), evalu(rhs)):
                pc = goto[dest]
        elif typ == 'FOR':
            V, start, end, step = args
            variables[V] = evalu(start)
            fors[V] = ForState(pc, evalu(end), evalu(step))
        elif typ == 'NEXT':
            V = args[0]
            continu, end, step = fors[V]
            if ((step >= 0 and variables[V] + step <= end) or
                (step <  0 and variables[V] + step >= end)):
                variables[V] += step
                pc = continu
        elif typ == 'GOSUB':
            ret = pc
            pc  = goto[args[0]]
        elif typ == 'RETURN':
            pc = ret

def preprocess(stmts):
    """Go through stmts and return two values extracted from the declarations: 
    functions: a mapping of {name: function}, for both built-in and user-defined functions,
    data:      a queue of all the numbers in DATA statements."""
    functions = {  # A mapping of {name: function}; first the built-ins:
        'SIN': math.sin, 'COS': math.cos, 'TAN': math.tan, 'ATN': math.atan, 
        'ABS': abs, 'EXP': math.exp, 'LOG': math.log, 'SQR': math.sqrt, 'INT': int,
        '>': op.gt, '<': op.lt, '=': op.eq, '>=': op.ge, '<=': op.le, '<>': op.ne, 
        '^': pow, '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv, '%': op.mod,
        'RND': lambda _: random.random(), 'NEG': op.neg}
    data = deque() # A queue of numbers that READ can read from
    for (_, typ, args) in stmts:
        if typ == 'DEF':
            name, parm, body = args
            functions[name] = Function(parm, body)
        elif typ == 'DATA':
            data.extend(args[0])
    return functions, data

def evalu(exp):
    "Evaluate an expression, returning a number."
    if isinstance(exp, Opcall):
        return functions[exp.op](evalu(exp.x), evalu(exp.y))
    elif isinstance(exp, Funcall):
        return functions[exp.f](evalu(exp.x))
    elif isinstance(exp, Subscript):
        return variables[exp.var, tuple(evalu(x) for x in  exp.indexes)]
    elif is_varname(exp):
        return variables[exp]
    else: # number constant
        return exp
    
def let(V, value):
    "Assign value to the variable name or Subscripted variable."
    if isinstance(V, Subscript): # A subsscripted variable
        variables[V.var, tuple(evalu(x) for x in V.indexes)] = value 
    else:                        # An unsubscripted variable
        variables[V] = value

def basic_print(items): 
    "Print the items (',' / ';' / label / expression) in appropriate columns."
    for item in items:
        if item == ',':      pad(15)
        elif item == ';':    pad(3)
        elif is_label(item): print_string(item.replace('"', ''))
        else:                print_string("{:g} ".format(evalu(item)))
    if (not items) or items[-1] not in (',', ';'):
        newline()
        
def print_string(s): 
    "Print a string, keeping track of column, and advancing to newline if at or beyond column 100."
    global column
    print(s, end='')
    column += len(s)
    if column >= 100: newline()
        
def pad(width): 
    "Pad out to the column that is the next multiple of width."
    while column % width != 0: 
        print_string(' ')

def newline(): global column; print(); column = 0

grammar = Grammar()

parse(program)

run(program)