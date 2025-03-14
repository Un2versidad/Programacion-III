# Hecho con Pycharm (Problema #1)
class Persona:
    def __init__(self):
        self.nombre = "Ana"
        self.edad = 18
        self.genero = "F".upper()

    def mostrar_datos(self):
        print("\nDatos de la persona:")
        print(f"Nombre: {self.nombre}")
        print(f"Género: {self.genero}")
        print(f"Edad: {self.edad}")

    def verificar_mayor_edad_y_genero(self):
        if self.edad >= 18 and self.genero == "F":
            print(f"{self.nombre} es mayor de edad y su género es F.")
        elif self.edad >= 18:
            print(f"{self.nombre} es mayor de edad pero su género no es F.")
        else:
            print(f"{self.nombre} no es mayor de edad.")

persona = Persona()
persona.mostrar_datos()
persona.verificar_mayor_edad_y_genero()