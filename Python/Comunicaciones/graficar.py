import numpy as np
import matplotlib.pyplot as plt

def serie_fourier(t, N):
    """
    Calcula la serie de Fourier para una función impar usando la expresión dada,
    sumando hasta N términos.
    
    Parámetros:
    - t: array-like, valores del dominio.
    - N: número de términos a sumar.
    
    Retorna:
    - y: array-like, valores de la serie de Fourier.
    """
    y = np.zeros_like(t)
    for n in range(1, N + 1):
        term = ( (119 / (50*n * np.pi)) - (5/(2*(n**2)*((np.pi)**2)))  ) * np.cos(n * t) + ( (-167 / (50*n * np.pi)) + (243/(2500*(n**2)*((np.pi)**2)))  ) * np.sin(n * t)
        y += term
    return (8/5) + y

def graficar_serie_fourier(N, xlim=None, ylim=None):
    """Grafica la serie de Fourier para una función impar usando N términos,
    con límites opcionales para los ejes x e y."""
    # Definir el dominio
    t = np.linspace(-10, 10, 1000)  # Ajusta el rango del dominio
    
    # Calcular la serie de Fourier
    y = serie_fourier(t, N)
    
    # Graficar
    plt.figure(figsize=(12, 8))
    plt.plot(t, y, label=f'Serie de Fourier con {N} términos')
    
    # Configurar límites de los ejes si se proporcionan
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)
    
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.title('Serie de Fourier para una función')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parámetro
N = 5  # Número de términos en la serie de Fourier

# Definir los límites de los ejes (opcional)
xlim = (-10, 10)  # Límites del eje t
ylim = (-5, 5)    # Límites del eje y (ajustar según el rango de tus datos)

# Graficar la función resultante con el número de términos dados y límites opcionales
graficar_serie_fourier(N, xlim=xlim, ylim=ylim)
