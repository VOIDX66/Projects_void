import sympy as sp

# Define todas las variables necesarias
n, w, t = sp.symbols('n w t')
T = 3

# Define las integrales
#an = sp.integrate((2*t + 8)*sp.cos(n * w * t), (t, -5, -4)) + sp.integrate((-2*t - 6)*sp.cos(n * w * t), (t, -3, -2)) + sp.integrate((-2)*sp.cos(n * w * t), (t, -2, 0))
an = (1/10)*(sp.integrate(sp.cos(t *(1 + n * w)), (t, -sp.pi/2, sp.pi/2)) + sp.integrate(sp.cos(t *(1 - n * w)), (t, -sp.pi/2, sp.pi/2)))
bn = sp.integrate((2*t + 8)*sp.sin(n * w * t), (t, -5, -4)) + sp.integrate((-2*t - 6)*sp.sin(n * w * t), (t, -3, -2)) + sp.integrate((-2)*sp.sin(n * w * t), (t, -2, 0))
cn = (
        sp.integrate((2*t + 2) * sp.exp(-sp.I * n * w * t), (t, -1, -0)) +
        sp.integrate((-2*t + 2) * sp.exp(-sp.I * n * w * t), (t, 0, 1))
        )
# Reescribe la expresión, asumiendo que m*w != 0 para eliminar el Piecewise
am_no_piecewise = an.rewrite(sp.Piecewise).subs(sp.Ne(n * w, 0), True).simplify()
bm_no_piecewise = bn.rewrite(sp.Piecewise).subs(sp.Ne(n * w, 0), True).simplify()
cm_no_piecewise = cn.rewrite(sp.Piecewise).subs(sp.Ne(n * w, 0), True).simplify()

print("am:", am_no_piecewise)
print("bm:", bm_no_piecewise)
print("cm:", cm_no_piecewise)
