'''
Esta es una solución al problema de Misiones y Canibales.
Usa una búsqueda primero en anchura.
'''
from __future__  import annotations
from dataclasses import dataclass, field
from copy        import deepcopy
from collections import deque
from graphviz    import Digraph

import sys
import time

@dataclass
class Time:
  start : float = time.time()

  def elapse(self):
    return time.time() - self.start


start = Time()

@dataclass
class State:
  missionaries : int
  cannibals    : int
  boats        : int

  def successors(self):
    if self.boats == 1:
      sgn = -1
      direction = 'de orilla inicial a la otra orilla'
    else:
      sgn = 1
      direction = 'de regreso a orilla original'
    for m in range(3):
      for c in range(3):
        new_state = State(self.missionaries+sgn*m, self.cannibals+sgn*c, self.boats+sgn*1);
        if m+c >= 1 and m+c <= 2 and new_state.is_valid():    # check whether action and resulting state are valid
          action = f'toma: {m} misioneros y {c} canibales {direction}. {new_state}'
          yield action, new_state

  def is_valid(self):
    # first check the obvious
    if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3 or (self.boats != 0 and self.boats != 1):
      return False
    # then check whether missionaries outnumbered by cannibals
    if self.cannibals > self.missionaries and self.missionaries > 0:    # more cannibals then missionaries on original shore
      return False
    if self.cannibals < self.missionaries and self.missionaries < 3:    # more cannibals then missionaries on other shore
      return False
    return True

  def is_goal(self):
    return self.cannibals == 0 and self.missionaries == 0 and self.boats == 0

@dataclass
class Node:
  parent : Node
  state  : State
  action : str
  depth  : int

  def expand(self):
    for (action, succ_state) in self.state.successors():
      succ_node = Node(
        parent = self,
        state = succ_state,
        action = action,
        depth=self.depth + 1)
      yield succ_node

  def extract_soluction(self):
    solution = []
    node = self
    while node.parent is not None:
      solution.append(node.action)
      node = node.parent
    solution.reverse()
    return solution

def bfs(state):
  root = Node(
    parent = None,
    state  = state,
    action = None,
    depth  = 0)
  fifo = deque([root])
  num_expansions = 0
  max_depth = -1

  while True:
    if not fifo:
      print(f'{num_expansions} expansiones')
      return None
    node = fifo.popleft()
    if node.depth > max_depth:
      max_depth = node.depth
      print(f'[profundidad = {max_depth}] {start.elapse():.2f}s')
    if node.state.is_goal():
      print(f'{num_expansions} expansiones')
      return node.extract_soluction()

    num_expansions += 1
    fifo.extend(node.expand())


def main():
  init  = State(3,3,1)
  sol   = bfs(init)
  if sol is None:
    print('sin solucion')
  else:
    print(f'solución ({len(sol):d}):')
    for s in sol:
      print(f'{s}')

  print(f'tiempo transcurrido: {start.elapse():.2f}s')

if __name__ == '__main__':
  main()
