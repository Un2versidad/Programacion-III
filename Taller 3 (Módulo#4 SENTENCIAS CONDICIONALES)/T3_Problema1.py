# CALCULADORA DE SALARIO SEMANAL (Hecho con Pycharm)
print("+" + "-" * 50 + "+")
print("|" + " " * 10 + "CALCULADORA DE SALARIO SEMANAL" + " " * 10 + "|")
print("+" + "-" * 50 + "+")
print("\nBienvenido al sistema de cálculo de salarios.\n")

# Entrada del nombre del empleado
while True:
    nombre = input("Ingrese el nombre del empleado: ").strip()
    if not nombre:
        print("\n❌ Error: El nombre del empleado no puede estar vacío. Por favor, intente nuevamente.\n")
    else:
        break

# Entrada de las horas trabajadas
while True:
    try:
        horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas en la semana: "))
        if horas_trabajadas < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas.")
        break
    except ValueError as e:
        print(f"\n❌ Error: {e}. Por favor, intente nuevamente.\n")

# Entrada de la rata por hora
while True:
    try:
        rata_por_hora = float(input("Ingrese la rata por hora: "))
        if rata_por_hora <= 0:
            raise ValueError("La rata por hora debe ser un valor positivo.")
        break
    except ValueError as e:
        print(f"\n❌ Error: {e}. Por favor, intente nuevamente.\n")

# Constantes
HORAS_NORMALES = 40
FACTOR_EXTRA = 2

# Cálculo del salario
if horas_trabajadas <= HORAS_NORMALES:
    salario_semanal = horas_trabajadas * rata_por_hora
else:
    horas_extras = horas_trabajadas - HORAS_NORMALES
    salario_semanal = (HORAS_NORMALES * rata_por_hora) + (horas_extras * rata_por_hora * FACTOR_EXTRA)

# Salida de resultados
print("\n" + "=" * 50)
print("                    RESULTADOS")
print("=" * 50)
print(f"Empleado: {nombre}")
print(f"Horas trabajadas: {horas_trabajadas:.2f} horas")
print(f"Rata por hora: ${rata_por_hora:.2f}")
print(f"Salario semanal: ${salario_semanal:.2f}")
print("\nGracias por usar el sistema de cálculo de salarios. ¡Hasta pronto!")