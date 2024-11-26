# stdlib.py
from abc     import ABC, abstractmethod
from pathlib import Path

import math
import statistics
import time


# ----------------------------------------
# clases abstractas
#
class CallError(Exception):
  pass


class BuiltinFunction(ABC):  # pragma: no cover
  '''
  Base class for MiniC builtin function.
  '''
  _shortname: str

  @property
  @abstractmethod
  def arity(self) -> int:
    raise NotImplementedError

  @abstractmethod
  def __call__(self, interp, *args):
    raise NotImplementedError

  def __str__(self) -> str:
    return f"<builtin {self._shortname}>"

# ----------------------------------------
# Generals
#
class Chr(BuiltinFunction):
  _shortname = "chr"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    '''
    if not isinstance(args[0], int):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return chr(args[0])


class Clock(BuiltinFunction):
  _shortname = "clock"

  @property
  def arity(self) -> int:
    return 0

  def __call__(self, _, *args):
    '''
    Return the time in seconds since the
    epoch as a floating point number.
    '''
    return time.time()


class Format(BuiltinFunction):
  _shortname = "format"

  @property
  def arity(self) -> int:
    return -1

  def __call__(self, _, *args):
    '''
    '''
    if len(args) < 2:
      raise CallError("Error en argumento de 'format'")
    if args[0].count('%') != len(args[1:]):
      raise CallError("Error en argumento de 'format'")
    if not isinstance(args[0], str):
      raise CallError("El 1er argumento de 'format' es incorrecto")
    format = args[0].replace('\\n', '\n')
    format = args[0].replace('\\t', '\t')
    return format % args[1:]


class Input(BuiltinFunction):
  _shortname = "input"

  @property
  def arity(self) -> int:
    return -1

  def __call__(self, _, *args):
    '''
    Prompt the user for a line of input using the provided prompt.
    '''
    if len(args) == 0:
      return input()
    elif len(args) == 1:
      if not isinstance(args[0], str):
        raise CallError(f"Argumento de '{self._shortname}' debe ser String")
      return input(args[0])

    raise CallError(f"Error en argumentos de '{self._shortname}'")


class Integer(BuiltinFunction):
  _shortname = 'int'

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    Convert a number or string to an integer.
    '''
    if not isinstance(args[0], (int, float, str)):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return int(args[0])


class Ord(BuiltinFunction):
  _shortname = "ord"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args) -> int:
    '''
    Return an integer representing the
    Unicode code point of the input
    character.
    '''
    if not isinstance(args[0], str):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return ord(args[0])


class ReadText(BuiltinFunction):
  _shortname = "read_text"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args) -> str:
    '''
    Return the contents of the specified
    file as a string.
    '''
    return Path(args[0]).read_text()


class String(BuiltinFunction):
  _shortname = 'str'

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    '''
    if not isinstance(args[0], (int, float)):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return str(args[0])


# ----------------------------------------
# math
#
class Abs(BuiltinFunction):
  _shortname = "abs"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    Return the absolute value of a number.
    '''
    if not isinstance(args[0], (int, float)):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return math.fabs(args[0])


class Ceil(BuiltinFunction):
  _shortname = "ceil"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args) -> int:
    '''
    Return the smallest number greater
    than or equal to the input value.
    '''
    if not isinstance(args[0], float):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return math.ceil(args[0])


class Cos(BuiltinFunction):
  _shortname = "cos"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    Return the cosine of x (measured in radians).
    '''
    if not isinstance(args[0], (int, float)):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return math.cos(args[0])


class Exp(BuiltinFunction):
  _shortname = "exp"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    if not isinstance(args[0], (int, float)):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return math.exp(args[0])


class Floor(BuiltinFunction):
  _shortname = "floor"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    Return the smallest number less than
    or equal to the input value.
    '''
    if not isinstance(args[0], float):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return math.floor(args[0])


class Log(BuiltinFunction):
  _shortname = "log"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    Returns the natural logarithm (base e) of x.
    '''
    if not isinstance(args[0], (int, float)):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return math.log(args[0])


class Log10(BuiltinFunction):
  _shortname = "log10"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    Return the base 10 logarithm of x.
    '''
    if not isinstance(args[0], (int, float)):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return math.log10(args[0])


class Power(BuiltinFunction):
  _shortname = "pow"

  @property
  def arity(self) -> int:
    return 2

  def __call__(self, _, *args):
    '''
    Return x power y.
    '''
    if not (isinstance(args[0], (int, float)) and isinstance(args[1], (int, float))):
      raise CallError(f"Los argumentos de '{self._shortname}' son incorrectos")
    return pow(args[0], args[1])


class Sin(BuiltinFunction):
  _shortname = "sin"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    Return the sine of x (measured in radians).
    '''
    if not isinstance(args[0], (int, float)):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return math.sin(args[0])


class Sqrt(BuiltinFunction):
  _shortname = "sqrt"

  @property
  def arity(self) -> int:
    return 1

  def __call__(self, _, *args):
    '''
    Return the square root of x.
    '''
    if not isinstance(args[0], (int, float)):
      raise CallError(f"El argumento de '{self._shortname}' es incorrecto")
    return math.sqrt(args[0])



consts = {
  'PI':    3.14159265358979323846,
  'E':     2.71828182845904523536,
  'GAMMA': 0.57721566490153286060,  # Euler
  'DEG':  57.29577951308232087680,  # deg/radian
  'PHI':   1.61803398874989484820,  # golden ratio
}

builtins = {
  # general
  'chr'   : Chr(),
  'clock' : Clock(),
  'format': Format(),
  'input' : Input(),
  'int'   : Integer(),
  'ord'   : Ord(),
  'read_text': ReadText(),
  'str'   : String(),

  # math
  'abs'   : Abs(),
  'ceil'  : Ceil(),
  'cos'   : Cos(),
  'exp'   : Exp(),
  'floor' : Floor(),
  'log'   : Log(),
  'log10' : Log10(),
  'pow'   : Power(),
  'sin'   : Sin(),
  'sqrt'  : Sqrt(),

  # regexp
  # stats
}

'''
builtins = {
        'atan':  math.atan,
        'asin':  math.asin,
        'acos':  math.acos,
        'sinh':  math.sinh,
        'cosh':  math.cosh,
        'tanh':  math.tanh,
}

class Max(BuiltinFunction):
    _shortname = "max"

    @property
    def arity(self) -> int:
        return 2

    def call(self, interpreter: SourceInterpreterProtocol, arguments: list[NUMERIC]) -> NUMERIC:
        """Return the maximum of the two values."""
        return max(arguments)


class Mean(BuiltinFunction):
    _shortname = "mean"

    @property
    def arity(self) -> int:
        return 1

    def call(self, interpreter: SourceInterpreterProtocol, arguments: list[LoxArray]) -> float:
        """Return the sample arithmetic mean of the data in the input `LoxArray`."""
        return statistics.mean(arguments[0].fields)


class Median(BuiltinFunction):
    _shortname = "median"

    @property
    def arity(self) -> int:
        return 1

    def call(self, interpreter: SourceInterpreterProtocol, arguments: list[LoxArray]) -> float:
        """
        Return the median (middle value) of the input `LoxArray`.
        If the input array contains an even number of data points, the median is interpolated by
        taking the average of the two middle values.
        """
        return statistics.median(arguments[0].fields)


class Min(BuiltinFunction):
    _shortname = "min"

    @property
    def arity(self) -> int:
        return 2

    def call(self, interpreter: SourceInterpreterProtocol, arguments: list[NUMERIC]) -> NUMERIC:
        """Return the minimum of the two values."""
        return min(arguments)


class Mode(BuiltinFunction):
    _shortname = "mode"

    @property
    def arity(self) -> int:
        return 1

    def call(self, interpreter: SourceInterpreterProtocol, arguments: list[LoxArray]) -> float:
        """Return the single most common data point from the input `LoxArray`."""
        return statistics.mode(arguments[0].fields)

class ReSub(BuiltinFunction):
    _shortname = "re_sub"

    @property
    def arity(self) -> int:
        return 3

    def call(self, interpreter: SourceInterpreterProtocol, arguments: list[str]) -> str:
        """Replace the leftmost non-overlapping occurrences of the pattern in the given string."""
        return re.sub(arguments[0], arguments[1], arguments[2])


class Std(BuiltinFunction):
    _shortname = "std"

    @property
    def arity(self) -> int:
        return 1

    def call(self, interpreter: SourceInterpreterProtocol, arguments: list[LoxArray]) -> float:
        """Return the sample standard deviation of the input `LoxArray`."""
        return statistics.stdev(arguments[0].fields)


class Str2Num(BuiltinFunction):
    _shortname = "str2num"

    @property
    def arity(self) -> int:
        return 1

    def call(self, interpreter: SourceInterpreterProtocol, arguments: list[str]) -> NUMERIC:
        """Convert the provided string into an integer or float."""
        try:
            return int(arguments[0])
        except ValueError:
            try:
                return float(arguments[0])
            except ValueError:
                pass

        raise ValueError(f"Cannot convert '{arguments[0]}' to an integer or float.")
'''

