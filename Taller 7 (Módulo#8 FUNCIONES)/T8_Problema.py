# Hecho Con Pycharm

#Se crea la lista con los datos de los primeros 15 días del mes de marzo
datos = [11,7,4,4,6,8,7,7,5,4,4,6,15,18,10]

#Se crea la función para calcular el promedio

def calcular_promedio(datos):
    suma = 0
    for i in range(0,len(datos)):
        suma = suma + datos[i]
    promedio = suma/len(datos)
    return promedio

#Se llama a la función para calcular el promedio
print("El promedio de la velocidad del viento es: ", calcular_promedio(datos))