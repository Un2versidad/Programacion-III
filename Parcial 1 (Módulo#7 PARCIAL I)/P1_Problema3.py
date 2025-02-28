# Hecho con Pycharm (Problema N°3)

print("Bienvenido a la sala de juegos Python, S.A." + "\n")
# Bucle para repetir el programa
while True:
  # Validacion de la edad (Evita la entrada de letras))
  try: 
    edad = int(input("Ingrese su edad: "))

    # Validacion de la edad (Evita la entrada de numeros negativos y edad superior a 100))
    if (edad < 1 or edad > 100):
      print("La edad no puede ser negativa, ´0´ o mayor a 100! Intente de nuevo.")
      raise ValueError

    #Condicional para determinar el precio de la entrada
    if edad < 4:
      print("Puede entrar gratis")
    elif edad >= 4 and edad <= 18:
     print("Debe pagar B/.5.00")
    else:
      print("Debe pagar B/.10.00")
  except ValueError:
    print("!Por favor ingrese un valor válido!\n")
