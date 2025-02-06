# Se utilizo de IDE Pycharm
from typing import Dict, Tuple

# Constantes
TASAS_CAMBIO: Dict[str, float] = {
    "dólares": 1.21,
    "colones": 738.59,
    "lempiras": 29.16,
    "pesos colombianos": 4314.00
}

def obtener_moneda() -> Tuple[str, float]:
    """
    Solicita al usuario seleccionar la moneda y la cantidad a cambiar.

    :return: Tupla con el nombre de la moneda y la cantidad a cambiar.
    """
    print("Seleccione la moneda que desea cambiar a euros:")
    for i, (moneda, tasa) in enumerate(TASAS_CAMBIO.items(), start=1):
        print(f"{i}. {moneda.capitalize()}")

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

    while True:
        try:
            cantidad = float(input(f"Ingrese la cantidad de {moneda} que desea cambiar a euros: "))
            if cantidad < 0:
                print("Error: La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    return moneda, cantidad

def convertir_a_euros(moneda: str, cantidad: float) -> float:
    """
    Convierte una cantidad de moneda a euros.

    :param moneda: Nombre de la moneda.
    :param cantidad: Cantidad a convertir.
    :return: Cantidad equivalente en euros.
    """
    return cantidad / TASAS_CAMBIO[moneda]

def mostrar_resultado(nombre: str, moneda: str, cantidad: float, cantidad_euros: float):
    """
    Muestra el resultado del cambio de moneda.

    :param nombre: Nombre del usuario.
    :param moneda: Moneda original.
    :param cantidad: Cantidad en la moneda original.
    :param cantidad_euros: Cantidad en euros.
    """
    print("\n--- Resumen del Cambio ---")
    print(f"Nombre: {nombre}")
    print(f"Cantidad en {moneda}: {cantidad:.2f}")
    print(f"Cantidad en euros: {cantidad_euros:.2f}")
    print("Gracias por utilizar nuestro servicio de cambio de moneda.")

def main():
    # Solicitar nombre del usuario
    nombre = input("Ingrese su nombre: ")

    # Obtener moneda y cantidad
    moneda, cantidad = obtener_moneda()

    # Convertir a euros
    cantidad_euros = convertir_a_euros(moneda, cantidad)

    # Mostrar resultado
    mostrar_resultado(nombre, moneda, cantidad, cantidad_euros)


if __name__ == "__main__":
    main()