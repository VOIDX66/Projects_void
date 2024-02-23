from simpleai.search import SearchProblem, depth_first, breadth_first
from rich import print

class CannibalsProblem(SearchProblem):
  '''Missioners and cannibals problem.'''

  def __init__(self):
    super(CannibalsProblem, self).__init__(initial_state=(3, 3, 0))
    # each action has a printable text, and the number of missioners
    # and cannibals to move on that action
    self._actions = [('1c', (0,1)),
                     ('1m', (1, 0)),
                     ('2c', (0, 2)),
                     ('2m', (2, 0)),
                     ('1m1c', (1, 1))]

  def actions(self, s):
    '''Possible actions from a state.'''
    # we try to generate every possible state and then filter those
    # states that are valid
    return [a for a in self._actions if self._is_valid(self.result(s, a))]

  def _is_valid(self, s):
    '''Check if a state is valid.'''
    # valid states: no more cannibals than missioners on each side,
    # and numbers between 0 and 3
    return ((s[0] >= s[1] or s[0] == 0)) and \
            ((3 - s[0]) >= (3 - s[1]) or s[0] == 3) and \
            (0 <= s[0] <= 3) and \
            (0 <= s[1] <= 3)

  def result(self, s, a):
    '''Result of applying an action to a state.'''
    # result: boat on opposite side, and numbers of missioners and
    # cannibals updated according to the move
    if s[2] == 0:
      return (s[0] - a[1][0], s[1] - a[1][1], 1)
    else:
      return (s[0] + a[1][0], s[1] + a[1][1], 0)

  def is_goal(self, state):
    return state == (0, 0, 1)
 
  def value(self, state):
    return 6 - state[0] - state[1]


problem = CannibalsProblem()

result = breadth_first(problem)
print(result.path())