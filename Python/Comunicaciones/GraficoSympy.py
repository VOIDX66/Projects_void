import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

a,b = sym.symbols('a b', constan = True)
t = sym.Symbol('t', real = True)
xt = a*sym.sin(t)+b*sym.sin(2*t)

sym.plot(xt.subs(a,1).subs(b,1))