import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Variables simbólicas
t, n = sp.symbols('t n', real=True)
T = 3  # Periodo
A = 2
w = (2 * sp.pi) / T

def calcular_coeficientes_fourier(N):
    """
    Calcula los coeficientes c_n de la serie de Fourier para N términos a partir de la función por intervalos.
    
    Parámetros:
    - N: número de términos a considerar en la serie de Fourier.
    
    Retorna:
    - freqs: lista de frecuencias.
    - cns: lista de coeficientes c_n.
    """
    freqs = []
    cns = []

    for n_v in range(-N, N + 1):
        if n_v == 0:
            cn = (1/T) * abs(A)  # Ajusta esto según la integral de la función en n=0
        else:
            # Definición de c_n
            cn = (3/((n_v**2)*(sp.pi**2)))*(1-sp.cos( (2/3) * sp.pi * n_v))
            #cn = (1/T)*(
            #sp.integrate((2*t + 2) * sp.exp(-sp.I * n_v * w * t), (t, -1, 0)) +
            #sp.integrate((-2*t + 2) * sp.exp(-sp.I * n_v * w * t), (t, 0, 1))
            #)
            
        
        freqs.append(n_v)
        cns.append(cn)  # Convertimos la expresión a un valor numérico

    return freqs, cns

def reconstruir_senal(N, T, t_vals):
    """
    Reconstruye la señal a partir de los coeficientes de Fourier.
    
    Parámetros:
    - N: número de términos en la serie de Fourier.
    - T: periodo de la señal.
    - t_vals: valores de tiempo donde se evalúa la señal.
    
    Retorna:
    - valores reconstruidos de la señal.
    """
    freqs, cns = calcular_coeficientes_fourier(N)
    w = (2 * np.pi) / T  # Frecuencia angular fundamental
    senal_reconstruida = np.zeros_like(t_vals, dtype=complex)
    
    for n, cn in zip(freqs, cns):
        # Convertir a número complejo y evaluar en cada t_val
        senal_reconstruida += np.array([complex(cn) * np.exp(1j * n * w * t_val) for t_val in t_vals])

    return senal_reconstruida.real

def graficar_senal_reconstruida(N, T):
    """Grafica solo la señal reconstruida a partir de la serie de Fourier."""    
    t_vals = np.linspace(-5, 0, 500)  # Rango de tiempo para la señal
    
    # Señal reconstruida
    senal_reconstruida = reconstruir_senal(N, T, t_vals)
    
    # Graficar la señal reconstruida
    plt.figure(figsize=(12, 6))
    plt.plot(t_vals, senal_reconstruida, label='Señal Reconstruida (Serie de Fourier)', color='blue')
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Señal Reconstruida a partir de Cn')
    plt.grid(True)
    plt.legend()
    plt.show()

# Parámetros
N = 10  # Número de términos en la serie de Fourier

# Calcular coeficientes y mostrarlos en consola
freqs, cns = calcular_coeficientes_fourier(N)
print("Coeficientes c_n:")
for n_val, cn in zip(freqs, cns):
    print(f"c_{n_val} = {cn}")

# Graficar la señal reconstruida
graficar_senal_reconstruida(N, T)
