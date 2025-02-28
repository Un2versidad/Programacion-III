# Hecho con Pycharm (Problema N°1)

# Diccionario con los precios de las frutas
precios_frutas = {
    "Guineos": 1.35,
    "Manzanas": 0.80,
    "Naranjas": 0.70,
    "Mandarinas": 0.60
}

print("Bienvenido a la Frutería Python, S.A.")
total = 0.0

# Imprimir listado de frutas y precios
print("\n---- Lista de Productos Disponibles ----\n")
for fruta, precio in precios_frutas.items():
  print(f"{fruta}: B/.{precio:.2f}")
print()

# Bucle para repetir el programa
while True:
    # Solicitar al usuario el nombre de la fruta y su peso
    fruta = input("Ingrese el nombre de la fruta (o 'salir' para terminar): ").capitalize()

    if fruta.lower() == "salir":
        break

    if fruta in precios_frutas:
        try:
          peso = float(input(f"Ingrese el peso en kg de {fruta}: "))
          if peso > 0:
              precio_total_fruta = peso * precios_frutas[fruta]
              total += precio_total_fruta
              print(f"Precio de {peso} kg de {fruta}: ${precio_total_fruta:.2f}")
          else:
              print("El peso debe ser mayor que cero.")
        except ValueError:
            print("Por favor, ingrese un valor numérico para el peso.")
    else:
        print(f"Lo siento, ´{fruta}´ no está disponible en nuestra tienda.")

# Mostrar el total de la compra
print(f"\nTotal de la compra: ${total:.2f}")
print("¡Gracias por su compra!")
