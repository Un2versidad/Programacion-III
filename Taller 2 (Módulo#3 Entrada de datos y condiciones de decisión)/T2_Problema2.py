# Problema 2 Conversión de Moneda a Euros (PyCharm)

# Constantes
TASAS_CAMBIO = {
    "dólares": 1.21,
    "colones": 738.59,
    "lempiras": 29.16,
    "pesos colombianos": 4314.00
}

print("=== Conversión de Moneda a Euros ===")

# Solicitar nombre del usuario
nombre = input("Ingrese su nombre: ")

# Mostrar opciones de moneda
print("\nSeleccione la moneda que desea cambiar a euros:")
for i, moneda in enumerate(TASAS_CAMBIO.keys(), start=1):
    print(f"{i}. {moneda.capitalize()}")

# Validar selección de moneda
while True:
    try:
        opcion = int(input("Ingrese el número correspondiente a la moneda: "))
        if 1 <= opcion <= len(TASAS_CAMBIO):
            moneda = list(TASAS_CAMBIO.keys())[opcion - 1]
            break
        else:
            print("Error: Opción no válida. Intente nuevamente.")
    except ValueError:
        print("Error: Ingrese un número válido.")

# Validar cantidad a cambiar
while True:
    try:
        cantidad = float(input(f"Ingrese la cantidad de {moneda} que desea cambiar a euros: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
        else:
            break
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

# Calcular cantidad en euros
cantidad_euros = cantidad / TASAS_CAMBIO[moneda]

# Mostrar resumen del cambio
print("\n--- Resumen del Cambio ---")
print(f"Nombre: {nombre}")
print(f"Cantidad en {moneda}: {cantidad:.2f}")
print(f"Cantidad en euros: {cantidad_euros:.2f}")
print("Gracias por utilizar nuestro servicio de cambio de moneda.")
