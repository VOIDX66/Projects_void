#!python2
# coding=utf-8

from __future__ import print_function

from simpleai.search import SearchProblem, breadth_first
from simpleai.search.viewers import WebViewer


class MissionersProblem(SearchProblem):
  '''
  Problema Misioneros y Canibales.
  '''

  def __init__(self):
    '''
    Cada acción tiene un texto imprimible y el número de misioneros y caníbales que
    se deben mover en esa acción.
    '''
    super(MissionersProblem, self).__init__(initial_state=(3, 3, 0))
    self._actions = [
      ('1c', (0,1)),
      ('1m', (1, 0)),
      ('2c', (0, 2)),
      ('2m', (2, 0)),
      ('1m1c', (1, 1))
    ]

  def actions(self, s):
    '''
    Posibles acciones de un estado
    
    Intentamos generar todos los estados posibles y luego filtrar aquellos que son válidos.
    '''
    return [a for a in self._actions if self._is_valid(self.result(s, a))]

  def _is_valid(self, s):
    '''
    Comprobar si un estado es válido.
    
    Estados válidos: no más caníbales que misioneros en cada bando y números entre 0 y 3.
    '''
    return (
      (s[0] >= s[1] or s[0] == 0) and 
      ((3 - s[0]) >= (3 - s[1]) or s[0] == 3) and 
      (0 <= s[0] <= 3) and 
      (0 <= s[1] <= 3))

  def result(self, s, a):
    '''
    Resultado de aplicar una acción a un estado
    
    Resultado: barco en el lado opuesto y números de misioneros y caníbales actualizados según el movimiento.
    '''
    if s[2] == 0:
      return (s[0] - a[1][0], s[1] - a[1][1], 1)
    else:
      return (s[0] + a[1][0], s[1] + a[1][1], 0)

  def is_goal(self, state):
    return state == (0, 0, 1)

  def heuristic(self, state):
    return (state[0] + state[1]) / 2

  def value(self, state):
    return 6 - state[0] - state[1]


problem = MissionersProblem()

result = breadth_first(problem , viewer=WebViewer())
print(result.path())