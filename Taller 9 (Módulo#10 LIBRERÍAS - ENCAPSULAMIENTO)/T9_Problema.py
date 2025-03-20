# Hecho con Pycharm 
# Fecha: 20/3/2025
import random
import matplotlib.pyplot as plt

# Paso 1: Generación de datos aleatorios
def generar_datos_aleatorios(n, minimo, maximo):
    """
    Genera una lista de n números aleatorios dentro del rango [minimo, maximo].

    Parámetros:
    - n: Número de datos a generar.
    - minimo: Valor mínimo del rango.
    - maximo: Valor máximo del rango.

    Retorna:
    - Una lista de números aleatorios.
    """
    return [random.randint(minimo, maximo) for _ in range(n)]


# Paso 2: Configuración de parámetros
num_datos = 50  # Número de datos a generar
rango_min = 10  # Valor mínimo del rango
rango_max = 100  # Valor máximo del rango

# Generar la lista de datos
datos_aleatorios = generar_datos_aleatorios(num_datos, rango_min, rango_max)


# Paso 3: Visualización de datos
def graficar_datos(datos):
    """
    Grafica los datos proporcionados en una gráfica de línea.

    Parámetros:
    - datos: Lista de datos a graficar.
    """
    indices = list(range(1, len(datos) + 1))  # Índices para el eje x
    plt.figure(figsize=(10, 6))
    plt.plot(indices, datos, marker='o', linestyle='-', color='b', label='Datos Aleatorios')
    plt.title('Gráfica de Datos Aleatorios')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.legend()
    plt.show()


# Mostrar la lista de datos generada
print("Datos Aleatorios Generados:", datos_aleatorios)

# Graficar los datos
graficar_datos(datos_aleatorios)
