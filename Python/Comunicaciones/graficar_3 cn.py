import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definir la variable simbólica
t = sp.symbols('t')

def calcular_coeficientes_fourier(N):
    """
    Calcula los coeficientes c_n de la serie de Fourier para N términos.
    
    Parámetros:
    - N: número de términos a considerar en la serie de Fourier.
    
    Retorna:
    - freqs: lista de frecuencias.
    - cns: lista de coeficientes c_n.
    """
    T = 4  # Periodo
    w = (2 * sp.pi) / T  # Frecuencia angular fundamental
    A = 3

    freqs = []
    cns = []

    for n in range(-N, N + 1):
        if n != 0:
            # Calcular c_n
            cn = (1/T)*(
                sp.integrate((2) * sp.exp(-sp.I * n * w * t), (t, 0, 1)) +
                sp.integrate((1) * sp.exp(-sp.I * n * w * t), (t, 1, 2))
            )
            freqs.append(n)  # Agregar frecuencia
            cns.append(cn)   # Agregar coeficiente
        else:
            # Definir c_0 como A/T
            freqs.append(n)
            cns.append(A / T)

    return freqs, cns

def graficar_espectro_frecuencias(N):
    """Grafica el espectro de frecuencias de la serie de Fourier."""
    
    # Calcular coeficientes
    freqs, cns = calcular_coeficientes_fourier(N)
    
    # Calcular la magnitud de los coeficientes
    magnitudes = [sp.Abs(cn).evalf() for cn in cns]

    # Filtrar las frecuencias y magnitudes para evitar valores complejos
    freqs_real = []
    magnitudes_real = []
    
    for freq, mag in zip(freqs, magnitudes):
        if mag.is_real:
            freqs_real.append(freq)
            magnitudes_real.append(float(mag))  # Convertir a flotante aquí

    # Imprimir información de depuración
    print("Frecuencias reales:", freqs_real)
    print("Magnitudes reales:", magnitudes_real)

    # Verificar si hay magnitudes reales
    max_magnitude = max(magnitudes_real) if magnitudes_real else 1  # Valor predeterminado si no hay magnitudes

    # Calcular w
    T = 3  # Periodo
    w = (2 * np.pi) / T  # Frecuencia angular fundamental

    # Graficar el espectro
    plt.figure(figsize=(12, 6))
    
    # Crear etiquetas en términos de pi
    labels = [f"${n} \\cdot \\frac{{2\\pi}}{{{T}}}$" for n in freqs_real]

    # Graficar con etiquetas formateadas
    plt.stem([freq * w for freq in freqs_real], magnitudes_real, basefmt=" ")  # Multiplicar por w
    plt.xlabel('Frecuencia ($n \\cdot \\frac{2\\pi}{T}$)')
    plt.ylabel('Magnitud |c_n|')
    plt.title('Espectro de Frecuencias de la Serie de Fourier')
    plt.grid(True)

    # Ajustar límites del eje x
    plt.xlim([-N * w, N * w])  

    plt.ylim(0, max_magnitude * 1.01)  # Para dar un poco de espacio en el gráfico

    # Personalizar etiquetas del eje x
    plt.xticks([freq * w for freq in freqs_real], labels)

    # Mostrar la gráfica
    plt.show()

# Parámetro
N = 10  # Número de términos en la serie de Fourier

# Graficar el espectro de frecuencias
graficar_espectro_frecuencias(N)
