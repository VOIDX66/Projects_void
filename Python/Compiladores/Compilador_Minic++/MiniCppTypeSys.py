# mctypesys.py
'''
Sistema de Tipos
================
Este archivo implementa las caracteristicas básicas del sistema de tipos.
Hay mucha flexibilidad posible aquí, pero la mejor estrategia podría ser
no pensar demasiado en el problema. Al menos no al principio.
Estos son los requisitos básicos mínimos:

1. Los tipos tienen identidad (por ejemplo, como mínimo un nombre como
   'int', 'float', 'bool')
2. Los tipos deben ser comparables. (por ejemplo, 'int' != 'float')
3. Los tipos admiten diferentes operadores (por ejemplo: +, -, *, /, etc.)

Una forma de lograr todos estos objetivos es comenzar con algun tipo de 
enfoque basado en tablas. No es lo mas sofisticado, pero funciona como
punto de partida.

Puede volver y refactorizar el sistema de tipos mas tarde.
'''
# Conjunto valido de typenames
typenames = {'int', 'float', 'bool', 'double', 'char', 'string'}

# Tabla de todas las operaciones binarias soportadas y el tipo resultante
_binary_ops = {
    # Operaciones int
    ('+', 'int', 'int') : 'int',
    ('-', 'int', 'int') : 'int',
    ('*', 'int', 'int') : 'int',
    ('/', 'int', 'int') : 'int',

    ('<',  'int', 'int') : 'bool',
    ('<=', 'int', 'int') : 'bool',
    ('>',  'int', 'int') : 'bool',
    ('>=', 'int', 'int') : 'bool',
    ('==', 'int', 'int') : 'bool',
    ('!=', 'int', 'int') : 'bool',

    # Operaciones float
    ('+', 'float', 'float') : 'float',
    ('-', 'float', 'float') : 'float',
    ('*', 'float', 'float') : 'float',
    ('/', 'float', 'float') : 'float',

    ('<',  'float', 'float') : 'bool',
    ('<=', 'float', 'float') : 'bool',
    ('>',  'float', 'float') : 'bool',
    ('>=', 'float', 'float') : 'bool',
    ('==', 'float', 'float') : 'bool',
    ('!=', 'float', 'float') : 'bool',

    # Bools
    ('&&', 'bool', 'bool') : 'bool',
    ('||', 'bool', 'bool') : 'bool',
    ('==', 'bool', 'bool') : 'bool',
    ('!=', 'bool', 'bool') : 'bool',

    # Double
    ('+', 'double', 'double') : 'double',
    ('-', 'double', 'double') : 'double',
    ('*', 'double', 'double') : 'double',
    ('/', 'double', 'double') : 'double',

    ('<',  'double', 'double') : 'bool',
    ('<=', 'double', 'double') : 'bool',
    ('>',  'double', 'double') : 'bool',
    ('>=', 'double', 'double') : 'bool',
    ('==', 'double', 'double') : 'bool',
    ('!=', 'double', 'double') : 'bool',

    # Char
    ('+', 'char', 'char') : 'string',
    ('+', 'char', 'string') : 'string',
    ('+', 'string', 'char') : 'string',
    ('==', 'char', 'char') : 'bool',
    ('!=', 'char', 'char') : 'bool',

    # String
    ('+', 'string', 'string') : 'string',
    ('==', 'string', 'string') : 'bool',
    ('!=', 'string', 'string') : 'bool',

    # Operaciones entre int y float
    ('+', 'int', 'float') : 'float',
    ('-', 'int', 'float') : 'float',
    ('*', 'int', 'float') : 'float',
    ('/', 'int', 'float') : 'float',

    ('+', 'float', 'int') : 'float',
    ('-', 'float', 'int') : 'float',
    ('*', 'float', 'int') : 'float',
    ('/', 'float', 'int') : 'float',

    ('<',  'int', 'float') : 'bool',
    ('<=', 'int', 'float') : 'bool',
    ('>',  'int', 'float') : 'bool',
    ('>=', 'int', 'float') : 'bool',
    ('==', 'int', 'float') : 'bool',
    ('!=', 'int', 'float') : 'bool',

    ('<',  'float', 'int') : 'bool',
    ('<=', 'float', 'int') : 'bool',
    ('>',  'float', 'int') : 'bool',
    ('>=', 'float', 'int') : 'bool',
    ('==', 'float', 'int') : 'bool',
    ('!=', 'float', 'int') : 'bool', 

    # Operaciones entre int y double
    ('+', 'int', 'double') : 'double',
    ('-', 'int', 'double') : 'double',
    ('*', 'int', 'double') : 'double',
    ('/', 'int', 'double') : 'double',

    ('+', 'double', 'int') : 'double',
    ('-', 'double', 'int') : 'double',
    ('*', 'double', 'int') : 'double',
    ('/', 'double', 'int') : 'double',

    ('<',  'int', 'double') : 'bool',
    ('<=', 'int', 'double') : 'bool',
    ('>',  'int', 'double') : 'bool',
    ('>=', 'int', 'double') : 'bool',
    ('==', 'int', 'double') : 'bool',
    ('!=', 'int', 'double') : 'bool',

    ('<',  'double', 'int') : 'bool',
    ('<=', 'double', 'int') : 'bool',
    ('>',  'double', 'int') : 'bool',
    ('>=', 'double', 'int') : 'bool',
    ('==', 'double', 'int') : 'bool',
    ('!=', 'double', 'int') : 'bool',

    # Operaciones entre float y double
    ('+', 'float', 'double') : 'double',
    ('-', 'float', 'double') : 'double',
    ('*', 'float', 'double') : 'double',
    ('/', 'float', 'double') : 'double',

    ('+', 'double', 'float') : 'double',
    ('-', 'double', 'float') : 'double',
    ('*', 'double', 'float') : 'double',
    ('/', 'double', 'float') : 'double',

    ('<',  'float', 'double') : 'bool',
    ('<=', 'float', 'double') : 'bool',
    ('>',  'float', 'double') : 'bool',
    ('>=', 'float', 'double') : 'bool',
    ('==', 'float', 'double') : 'bool',
    ('!=', 'float', 'double') : 'bool',

    ('<',  'double', 'float') : 'bool',
    ('<=', 'double', 'float') : 'bool',
    ('>',  'double', 'float') : 'bool',
    ('>=', 'double', 'float') : 'bool',
    ('==', 'double', 'float') : 'bool',
    ('!=', 'double', 'float') : 'bool', 
}

_unary_ops = {
    # Operaciones int
    ('+', 'int') : 'int',
    ('-', 'int') : 'int',

    # Operaciones float
    ('+', 'float') : 'float',
    ('-', 'float') : 'float',

    # Bools
    ('!', 'bool') : 'bool',
}

def loockup_type(name):
    '''
    Dado el nombre de un tipo primitivo, se busca el objeto "type" apropiado.
    Para empezar, los tipos son solo nombres, pero mas adelante pueden ser
    objetos mas avanzados.
    '''
    if name in typenames:
        return name
    else:
        return None
    
def check_binary_op(op, left, right):
    '''
    Revisa si una operacion binaria es permitida o no. Retorna el type
    resultante or None si no es soportado
    '''
    return _binary_ops.get((op, left, right))

def check_unary_op(op, expr):
    '''
    Revisa si una operacion unaria es permitida o no. Retorna el type
    resultante or None si no es soportado
    '''
    return _unary_ops.get((op, expr))