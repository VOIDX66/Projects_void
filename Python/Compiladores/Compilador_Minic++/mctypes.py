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
# types.py
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

