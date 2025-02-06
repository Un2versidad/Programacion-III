# FARMACIA XYZ - DESCUENTO PARA JUBILADOS (Hecho con Pycharm)
print("+" + "-" * 50 + "+")
print("|" + " " * 6 + "FARMACIA XYZ - DESCUENTO PARA JUBILADOS" + " " * 5 + "|")
print("+" + "-" * 50 + "+")
print("\nBienvenido al sistema de descuentos para jubilados.\n")

# Bucle para validar la entrada de datos
while True:
    try:
        precio_medicamento = float(input("Ingrese el precio del medicamento: "))
        if precio_medicamento <= 0:
            raise ValueError("El precio del medicamento debe ser un valor positivo.")
        break  # Salir del bucle si la entrada es válida
    except ValueError as e:
        print(f"\n❌ Error: {e}. Por favor, intente nuevamente.\n")

# Constante
DESCUENTO = 0.10

# Cálculo del descuento
descuento = precio_medicamento * DESCUENTO
precio_final = precio_medicamento - descuento

# Salida de resultados
print("\n" + "=" * 50)
print("                  RESULTADOS")
print("=" * 50)
print(f"Precio original del medicamento: ${precio_medicamento:.2f}")
print(f"Descuento aplicado (10%): ${descuento:.2f}")
print(f"Precio final con descuento: ${precio_final:.2f}")
print("\nGracias por usar el sistema de descuentos de Farmacia XYZ. ¡Hasta pronto!")