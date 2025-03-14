# Hecho con Pycharm (Problema #2)
class Empleados:
    def __init__(self):
        self.nombre = "Carlos"
        self.sueldoBruto = 19.22

    def mostrar(self) :
        print("Nombre: ", self.nombre)
        print("Sueldo Bruto: ", f"{self.sueldoBruto:.2f}", "$")

    def salario_neto(self):
        salario = self.sueldoBruto - (self.sueldoBruto * 0.17)
        salario = salario - (salario * 0.005)
        print("Salario Neto: ", f"{salario:.2f}", "$")

empleados = Empleados()
empleados.mostrar()
empleados.salario_neto()