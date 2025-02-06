# Se utilizo de IDE Pycharm
def ingresar_ventas(num_ventas: int) -> list[float]:
    """
    Solicita al usuario ingresar los valores de las ventas diarias.

    :param num_ventas: Número de ventas a ingresar.
    :return: Lista con los valores de las ventas.
    """
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
    return ventas

def calcular_promedio(ventas: list[float]) -> float:
    """
    Calcula el promedio de una lista de valores.

    :param ventas: Lista de valores de ventas.
    :return: Promedio de las ventas.
    """
    return sum(ventas) / len(ventas)

def comparar_promedio(promedio: float, valor_referencia: float) -> str:
    """
    Compara el promedio con un valor de referencia y devuelve un mensaje.

    :param promedio: Promedio de las ventas.
    :param valor_referencia: Valor de referencia para comparar.
    :return: Mensaje indicando si el promedio es mayor, menor o igual al valor de referencia.
    """
    if promedio > valor_referencia:
        return f"El promedio de ventas diarias (${promedio:.2f}) es MAYOR que ${valor_referencia:.2f}."
    elif promedio < valor_referencia:
        return f"El promedio de ventas diarias (${promedio:.2f}) es MENOR que ${valor_referencia:.2f}."
    else:
        return f"El promedio de ventas diarias (${promedio:.2f}) es IGUAL a ${valor_referencia:.2f}."

def main():
    # Constantes
    num_ventas = 5
    valor_referencia = 677.00

    # Ingresar ventas
    print("Ingrese los valores de las ventas diarias:")
    ventas = ingresar_ventas(num_ventas)

    # Calcular promedio
    promedio = calcular_promedio(ventas)

    # Comparar y mostrar resultado
    resultado = comparar_promedio(promedio, valor_referencia)
    print(resultado)

if __name__ == "__main__":
    main()