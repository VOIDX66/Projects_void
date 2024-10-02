import sympy as sp
from rich import print

class Serie_Fourier:
    @staticmethod
    def integrar(fuction, inf_limit, sup_limit):
        integral = sp.integrate(fuction, (t, inf_limit, sup_limit))
        return integral  # Devolver el resultado sin simplificación
    
t = sp.symbols('t')
w0 = sp.symbols('w0')
n = sp.symbols('n')

if __name__ == '__main__':

    funcion = 2*sp.cos(n*w0*t)
    resultado = Serie_Fourier.integrar(funcion, -1/5, 2)
    T = 16/5

    print((2/T)*resultado)

