
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
from dataclasses import dataclass, field
from typing      import Union, List

@dataclass
class CObject:
  def __repr__(self):
    return self.__str__()


@dataclass
class Number(CObject):
  value : Union[int, float]

  def __str__(self):
    return f'{self.value}'


@dataclass
class String(CObject):
  value : str

  def __str__(self):
    return f'{self.value}'


@dataclass
class Bool(CObject):
  value : bool

  def __str__(self):
    return f'{self.value}'


@dataclass
class Nil(CObject):
  value : str = 'nil'

  def __str__(self):
    return f'{self.value}'


@dataclass
class Array(CObject):
  _arr : List[CObject] = field(default_factory=list)

  def append(self, elem: CObject):
    self._arr.append(elem)

  def __len__(self):
    return len(self._arr)

  def __setitem__(self, elem:CObject, idx: int):
    if not 0 <= idx < len(self._arr):
      raise IndexError('idx esta fuera de limite')
    self._arr[idx] = elem

  def __getitem__(self, idx: int):
    if not 0 <= idx < len(self._arr):
      raise IndexError('idx esta fuera de limite')
    return self._arr[idx]

  def __str__(self):
    output : str = '['
    if len(self._arr) != 0:
      for elem in self._arr:
        output += str(elem) + ', '
      output = output[:-2]
    output += ']'
    return output


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
}

_unary_ops = {
    # Operaciones int
    ('+', 'int') : 'int',
    ('-', 'int') : 'int',

    # Operaciones float
    ('+', 'float') : 'float',
    ('-', 'float') : 'float',
}

valid_casts = {
    'int': {'float','string'},    # int puede venir de float, double, char
    'float': {'int','string'},    # float puede venir de int, double, char
    'double': {'int', 'float', 'string'},    # double puede venir de int, float, char
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
    if _binary_ops.get((op, left, right)) is None:
        #print(f"Operacion no soportada: {op} {left} {right}")
        return None
    else:
        return _binary_ops.get((op, right, left))

def check_unary_op(op, expr):
    '''
    Revisa si una operacion unaria es permitida o no. Retorna el type
    resultante or None si no es soportado
    '''
    unary = _unary_ops.get((op, expr))
    if unary is not None:
        return unary
    else:
        return None

#Checkear instruccion de Cast

def check_cast(target_type, source_type):
    # Define los cast válidos entre tipos

    if source_type in valid_casts.get(target_type, {}):
        return target_type
    else:
        #print(f"Error: No se puede castear de {source_type} a {target_type}")
        return None