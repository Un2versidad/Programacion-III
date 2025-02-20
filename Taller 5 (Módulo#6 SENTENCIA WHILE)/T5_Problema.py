# Sistema de Registro de Ventas Diarias (Pycharm)

print("=== Sistema de Registro de Ventas Diarias ===")

total_ventas = 0  # Acumulador para el total de ventas
num_clientes = 0  # Contador para el número de clientes atendidos

while True:
    # Preguntar si se desea registrar una venta
    respuesta = input("¿Desea registrar una venta? (s/n): ").strip().lower()

    if respuesta == 'n':  # Si el usuario responde "n", salir del bucle
        break
    elif respuesta == 's':  # Si el usuario responde "s", registrar la venta
        try:
            venta = float(input("Ingrese el monto de la venta: "))
            if venta < 0:
                print("El monto de la venta no puede ser negativo. Intente nuevamente.")
                continue

            total_ventas += venta  # Acumular el monto de la venta
            num_clientes += 1  # Incrementar el contador de clientes
            print(f"Venta registrada. Total acumulado: ${total_ventas:.2f}")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
    else:
        print("Respuesta no válida. Por favor, ingrese 's' para sí o 'n' para no.")

# Calcular el promedio de venta por cliente
if num_clientes > 0:
    promedio_venta = total_ventas / num_clientes
else:
    promedio_venta = 0

# Mostrar los resultados finales
print("\n=== Resumen del Día ===")
print(f"Cantidad de clientes atendidos: {num_clientes}")
print(f"Total de ventas: ${total_ventas:.2f}")
print(f"Promedio de venta por cliente: ${promedio_venta:.2f}")