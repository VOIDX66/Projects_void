import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Definir la variable simbólica
t = sp.symbols('t')

def serie_fourier_sympy(t, N):
    """
    Calcula la serie de Fourier de forma simbólica usando SymPy.
    
    Parámetros:
    - t: variable simbólica.
    - N: número de términos a sumar.
    
    Retorna:
    - y: expresión simbólica de la serie de Fourier.
    """
    y = 0
    T= 4
    w = (2*sp.pi)/T
    A = 3
    A_0 = (2*A)/T
    m = sp.symbols('m')

    # Sumar los términos de la serie de Fourier simbólica
    for n in range(1, N + 1):
        an =  (1 / (sp.pi*n)) * (sp.sin(n*w))
        bn =  (1 / (sp.pi*n)) * (-sp.cos(n*w) + 2 - (-1)**n )
        term = an*sp.cos(n*t*w) + bn*sp.sin(n*t*w)
        y += term
    return (A_0/2) + y

def graficar_serie_fourier_sympy(N, xlim=None, ylim=None):
    """Grafica la serie de Fourier calculada simbólicamente usando SymPy,
    con N términos, y opcionalmente con límites para los ejes x e y."""
    
    # Obtener la expresión simbólica de la serie de Fourier
    y_sympy = serie_fourier_sympy(t, N)
    
    # Convertir la expresión simbólica en una función numérica
    y_func = sp.lambdify(t, y_sympy, "numpy")
    
    # Definir el dominio numérico
    t_vals = np.linspace(-10, 10, 1000)
    
    # Evaluar la función numérica en los valores del dominio
    y_vals = y_func(t_vals)
    
    # Graficar la función numérica
    plt.figure(figsize=(12, 8))
    plt.plot(t_vals, y_vals, label=f'Serie de Fourier con {N} términos (SymPy)')
    
    # Configurar límites de los ejes si se proporcionan
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.title('Serie de Fourier para una función (usando SymPy)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parámetro
N = 100  # Número de términos en la serie de Fourier

# Definir los límites de los ejes (opcional)
xlim = (-1, 10)  # Límites del eje t
ylim = (-3, 3)    # Límites del eje y (ajustar según el rango de tus datos)

# Graficar la función resultante con el número de términos dados y límites opcionales
graficar_serie_fourier_sympy(N, xlim=xlim, ylim=ylim)
