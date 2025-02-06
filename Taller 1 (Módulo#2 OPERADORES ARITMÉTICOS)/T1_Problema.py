# Programación III - Taller 1 (PyCharm)
# Este programa abarca varios ejercicios de manejo de variables, listas y diccionarios en Python.

# Ejercicio 1: Manejo de variables con el intérprete de Python
# Asignaciones numéricas enteras y flotantes
numero_entero = 25  # Variable numérica entera
numero_flotante = 12.34  # Variable numérica flotante
print(f"El número entero es: {numero_entero}")
print(f"El número flotante es: {numero_flotante}")

# Creación y salida de una cadena de texto
texto = "¡Hola, mundo!"  # Cadena de texto
print(f"El texto creado es: {texto}")

# Conversión de valores a cadenas y envío a salida
numero_como_cadena = str(numero_entero)  # Conversión de entero a cadena
flotante_como_cadena = str(numero_flotante)  # Conversión de flotante a cadena
print(f"El número entero como cadena es: {numero_como_cadena}")
print(f"El número flotante como cadena es: {flotante_como_cadena}")

# Ejercicio 2: Crear una lista de países
paises = ["Argentina", "Brasil", "Chile", "Colombia", "Ecuador", "México", "Perú"]
print(f"Lista completa de países: {paises}")

# Enviar a salida el rango de posiciones de 0 a 5
print(f"Los países en las posiciones de 0 a 5 son: {paises[0:6]}")

# Ejercicio 3: Generar un diccionario con marca, año y color
vehiculo = {
    "marca": "Toyota",
    "año": 2024,
    "color": "Rojo"
}
print(f"Diccionario del vehículo: {vehiculo}")