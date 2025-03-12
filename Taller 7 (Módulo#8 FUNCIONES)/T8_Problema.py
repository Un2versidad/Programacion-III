# Hecho Con Pycharm

# Se crea la lista con los datos de los primeros 15 días del mes de marzo
datos = [11,7,4,4,6,8,7,7,5,4,4,6,15,18,10]

# Se crea la función para calcular el promedio
def calcular_promedio(datos):
    if not datos or len(datos) != 15:
        raise ValueError("Debe proporcionar exactamente 15 valores de velocidad del viento.")
    
    if any(v < 0 or v > 30 for v in datos):
        raise ValueError("Las velocidades deben estar en el rango de 0 a 30 km/h.")
    
    return sum(datos) / len(datos)

# Se llama a la función para calcular el promedio
print(f"El promedio de la velocidad del viento es: {calcular_promedio(datos):.2f} km/h")
