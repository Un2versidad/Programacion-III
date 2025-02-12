# Solicitar al usuario un número entero entre 1 y 10
while True:
    try:
        numero = int(input("Ingrese un número entero entre 1 y 10: "))
        if 1 <= numero <= 10:
            break  # Salir del bucle si el número es válido
        else:
            print("El número debe estar entre 1 y 10. Intente nuevamente.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Usar un bucle for para imprimir la tabla de multiplicar
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):  # Iterar desde 1 hasta 10 (inclusivo)
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
