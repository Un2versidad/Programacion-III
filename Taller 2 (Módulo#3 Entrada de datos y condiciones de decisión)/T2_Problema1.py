# Problema 1: Comparación de Ventas Diarias (Se uso Pycharm)

# Constantes
num_ventas = 5
valor_referencia = 677.00

print("=== Problema 1: Comparación de Ventas Diarias ===")
print("Ingrese los valores de las ventas diarias:")

# Ingresar ventas
ventas = []
for i in range(num_ventas):
    while True:
        try:
            venta = float(input(f"Ingrese el valor de la venta {i + 1}: "))
            if venta < 0:
                print("Error: El valor de la venta no puede ser negativo.")
            else:
                ventas.append(venta)
                break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

# Calcular promedio
promedio = sum(ventas) / len(ventas)

# Comparar y mostrar resultado
if promedio > valor_referencia:
    comparacion = f"El promedio de ventas diarias (${promedio:.2f}) es MAYOR que ${valor_referencia:.2f}."
elif promedio < valor_referencia:
    comparacion = f"El promedio de ventas diarias (${promedio:.2f}) es MENOR que ${valor_referencia:.2f}."
else:
    comparacion = f"El promedio de ventas diarias (${promedio:.2f}) es IGUAL a ${valor_referencia:.2f}."

print(f"\nEl promedio de las ventas diarias es: ${promedio:.2f}")
print(comparacion)
