import sympy as sp
from rich import print

class Serie_Fourier:
    @staticmethod
    def integrar(fuction, inf_limit, sup_limit):
        integral = sp.integrate(fuction, (t, inf_limit, sup_limit))
        return integral  # Devolver el resultado sin simplificación
    
    def calc_a0(functions, T):
        a0 = 0
        for function,lim_i, lim_s in functions:
            a0 += Serie_Fourier.integrar(function, (t, lim_i, lim_s))
        return (2/T) * a0

t = sp.symbols('t')
w0 = sp.symbols('w0')
n = sp.symbols('n')

if __name__ == '__main__':

    funciones = [(6*t-6, 0, sp.pi)]

    # Asegurarse de que no aparezcan "Piecewise" ni "Eq"
    #if isinstance(resultado, sp.Piecewise):
    #    resultado = resultado.args[1]  # Tomar solo la primera parte de la pieza

