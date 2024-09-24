
from simpleai.search import SearchProblem, deep

class MissionariesProblem(SearchProblem):
    '''Problemas de Misioneros y Canibales'''

    def __init__(self):
        self.action = [
            ("1c"),
            ("1m"),
            ("2c"),
            ("2m"),
            ("1m1c")
        ]
    
    def actions(self, s):
        return [a for in a in self._action if self_is_valid(self.result(s,0))]
    
    def _is_valid(self, s):
        return 