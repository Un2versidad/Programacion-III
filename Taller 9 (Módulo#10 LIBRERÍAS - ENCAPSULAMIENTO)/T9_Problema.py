import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Generación de datos aleatorios con NumPy
def generar_datos_aleatorios_numpy(n, minimo, maximo):
    """
    Genera una lista de n números aleatorios dentro del rango [minimo, maximo] usando NumPy.
    
    Parámetros:
    - n: Número de datos a generar.
    - minimo: Valor mínimo del rango.
    - maximo: Valor máximo del rango.
    
    Retorna:
    - Un array de números aleatorios.
    """
    return np.random.randint(minimo, maximo + 1, size=n)

# Paso 2: Configuración de parámetros
num_datos = 10000  # Aumentamos el número de datos para probar la eficiencia
rango_min = 10     # Valor mínimo del rango
rango_max = 100    # Valor máximo del rango

# Generar la lista de datos
datos_aleatorios = generar_datos_aleatorios_numpy(num_datos, rango_min, rango_max)

# Paso 3: Visualización eficiente con Matplotlib
def graficar_datos_eficiente(datos):
    """
    Grafica los datos proporcionados en una gráfica de línea de manera eficiente.
    
    Parámetros:
    - datos: Array de datos a graficar.
    """
    indices = np.arange(1, len(datos) + 1)  # Índices para el eje x usando NumPy
    plt.figure(figsize=(12, 6))
    plt.plot(indices, datos, marker=',', linestyle='-', color='b', label='Datos Aleatorios', alpha=0.7)
    plt.title('Gráfica de Datos Aleatorios (Optimizada)', fontsize=14)
    plt.xlabel('Índice', fontsize=12)
    plt.ylabel('Valor', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=10)
    plt.tight_layout()  # Ajusta automáticamente los márgenes
    plt.show()

# Mostrar los primeros 10 datos generados
print("Primeros 10 Datos Aleatorios Generados:", datos_aleatorios[:10])

# Graficar los datos
graficar_datos_eficiente(datos_aleatorios)