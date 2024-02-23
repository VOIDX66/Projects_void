import sympy as sym

t = sym.Symbol('t',real=True)
energia = sym.integrate((sym.exp(-t))**2,(t,0, sym.oo))

sym.pprint(energia)#oo