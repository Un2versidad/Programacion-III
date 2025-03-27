# Hecho con Pycharm
from datetime import date

class Animal:
    def __init__(self, nombre, especie, dueno):
        self.nombre = nombre
        self.especie = especie
        self.dueno = dueno

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - Dueño: {self.dueno}"

class Servicio:
    def __init__(self, fecha):
        self.fecha = fecha
        self.registro_peluqueria = []
        self.registro_clinica = []
        self.ventas_alimento = []

class Peluqueria:
    def __init__(self, animal, tipo_servicio):
        self.animal = animal
        self.tipo_servicio = tipo_servicio  # "baño" o "corte"

    def __str__(self):
        return f"{self.animal} - Servicio: {self.tipo_servicio}"

class AtencionClinica:
    def __init__(self, animal, diagnostico):
        self.animal = animal
        self.diagnostico = diagnostico

    def __str__(self):
        return f"{self.animal} - Diagnóstico: {self.diagnostico}"

class VentaAlimento:
    def __init__(self, producto, cantidad, precio):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.producto} - Cantidad: {self.cantidad} - ${self.precio}"

    def total(self):
        return self.cantidad * self.precio

class Veterinaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.servicio_dia = Servicio(date.today())

    def registrar_peluqueria(self, animal, tipo_servicio):
        servicio = Peluqueria(animal, tipo_servicio)
        self.servicio_dia.registro_peluqueria.append(servicio)
        print(f"Registrado: {servicio}")

    def registrar_clinica(self, animal, diagnostico):
        servicio = AtencionClinica(animal, diagnostico)
        self.servicio_dia.registro_clinica.append(servicio)
        print(f"Registrado: {servicio}")

    def registrar_venta_alimento(self, producto, cantidad, precio):
        venta = VentaAlimento(producto, cantidad, precio)
        self.servicio_dia.ventas_alimento.append(venta)
        print(f"Registrado: {venta}")

    def generar_reporte_diario(self):
        print(f"\n=== Reporte Diario - {self.nombre} - {self.servicio_dia.fecha} ===")

        # Reporte de Peluquería
        print("\nServicios de Peluquería:")
        if self.servicio_dia.registro_peluqueria:
            for servicio in self.servicio_dia.registro_peluqueria:
                print(f"- {servicio}")
        else:
            print("No hay servicios de peluquería registrados")

        # Reporte de Clínica
        print("\nAtenciones Clínicas:")
        if self.servicio_dia.registro_clinica:
            for atencion in self.servicio_dia.registro_clinica:
                print(f"- {atencion}")
        else:
            print("No hay atenciones clínicas registradas")

        # Reporte de Ventas
        print("\nVentas de Alimentos:")
        total_ventas = 0
        if self.servicio_dia.ventas_alimento:
            for venta in self.servicio_dia.ventas_alimento:
                print(f"- {venta}")
                total_ventas += venta.total()
            print(f"Total de ventas: ${total_ventas}")
        else:
            print("No hay ventas registradas")

vet = Veterinaria("PythonS.A")

# Crear algunos animales
perro1 = Animal("Max", "Perro", "Juan Pérez")
gato1 = Animal("Luna", "Gato", "María López")

# Registrar servicios
vet.registrar_peluqueria(perro1, "baño y corte")
vet.registrar_clinica(gato1, "Vacunación anual")
vet.registrar_venta_alimento("Alimento para perros", 2, 15000)
vet.registrar_venta_alimento("Alimento para gatos", 1, 12000)

# Generar reporte diario
vet.generar_reporte_diario()
