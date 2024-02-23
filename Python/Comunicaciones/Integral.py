import sympy as sym

t = sym.Symbol('t',real=True)
i1 = sym.integrate(1*sym.sin(t),(t,0,sym.pi))+sym.integrate(-1*sym.sin(t),(t,sym.pi,2*sym.pi))
i2 = sym.integrate(sym.sin(t)**2,(t,0,2*sym.pi))
solucion = i1/i2
sym.pprint(solucion)#oo