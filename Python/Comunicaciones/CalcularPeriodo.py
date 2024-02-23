import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def obtener_picos(funcion,t):
    xt = funcion
    # Encontrar todos los picos de la función
    peaks, _ = find_peaks(xt)
    if len(peaks) == 0:
        #print("No se encontraron picos en la función.")
        return None
    # Obtener las coordenadas (t, xt) de todos los picos
    picos_coordenadas = list(zip(t[peaks], xt[peaks]))

    return picos_coordenadas

def calc_periodo(funcion,t,graficar=False):
    todos_los_picos = obtener_picos(funcion,t)
    
    if graficar:
        # Graficar la función con los picos marcados
        xt = funcion
        plt.plot(t, xt)
        plt.scatter(*zip(*todos_los_picos), color='red', marker='o', label='Picos')
        plt.legend()
        plt.show()
    
    # Imprimir los picos
    periodo = 0
    if todos_los_picos is not None:
        #print("Coordenadas de los picos:")
        for t_pico1, xt_pico1 in todos_los_picos:
            for t_pico2,xt_pico2 in todos_los_picos:
                num1 = float(str(xt_pico1)[:4]) 
                num2 = float(str(xt_pico2)[:4])
                if num1 == num2 and t_pico1 != t_pico2:
                    periodo = abs(t_pico2-t_pico1)
                    return round(periodo,3)
    return 0

# Ejemplo de uso
a = b = 1
#t = t_inicial,t_final,tamaño_pasos
t = np.arange(0,4*np.pi,0.01)
#Funcion
mi_funcion = a*np.sin(2*t)+b*np.sin(np.pi*t)
resultado = calc_periodo(mi_funcion,t,True)
print(resultado)