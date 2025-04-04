# Hecho con Pycharm (Parcial 2)

class Producto:
    def __init__(self, referencia, nombre, descripcion, precio):
        self.referencia = referencia
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def es_caro(self):
        return self.precio > 10

    def mostrar(self):
        info = f"Referencia: {self.referencia}\nNombre: {self.nombre}\nPrecio: ${self.precio:.2f}"
        if self.descripcion:
            info += f"\nDescripción: {self.descripcion}"
        return info

class Alimento(Producto):
    def __init__(self, referencia, nombre, descripcion, precio, productor, distribuidor):
        super().__init__(referencia, nombre, descripcion, precio)
        self.productor = productor
        self.distribuidor = distribuidor

    def mostrar(self):
        return f"{super().mostrar()}\nProductor: {self.productor}\nDistribuidor: {self.distribuidor}"

class Libro(Producto):
    def __init__(self, referencia, nombre_libro, nombre_autor, isbn, distribuidor, precio):
        super().__init__(referencia, nombre_libro, None, precio)
        self.nombre_autor = nombre_autor
        self.isbn = isbn
        self.distribuidor = distribuidor

    def mostrar(self):
        return f"{super().mostrar()}\nAutor: {self.nombre_autor}\nISBN: {self.isbn}\nDistribuidor: {self.distribuidor}"

class Medicamento(Producto):
    def __init__(self, nombre, distribuidora, precio, farmaceutica):
        super().__init__(None, nombre, None, precio)
        self.distribuidora = distribuidora
        self.farmaceutica = farmaceutica

    def mostrar(self):
        return f"Nombre: {self.nombre}\nPrecio: ${self.precio:.2f}\nDistribuidora: {self.distribuidora}\nFarmacéutica: {self.farmaceutica}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrar_caros(self):
        caros = [p for p in self.productos if p.es_caro()]
        if not caros:
            print("\nNo hay productos con precio mayor a $10")
            return

        print("\n--- PRODUCTOS CON PRECIO > $10 ---")
        for producto in caros:
            print(f"\n{producto.mostrar()}\n" + "-" * 40)

def capturar_alimento():
    print("\nCapturar Alimento:")
    return Alimento(
        referencia=input("Referencia: "),
        nombre=input("Nombre: "),
        descripcion=input("Descripción: "),
        precio=float(input("Precio: $")),
        productor=input("Productor: "),
        distribuidor=input("Distribuidor: ")
    )

def capturar_libro():
    print("\nCapturar Libro:")
    return Libro(
        referencia=input("Referencia: "),
        nombre_libro=input("Nombre del libro: "),
        nombre_autor=input("Nombre del autor: "),
        isbn=input("ISBN: "),
        distribuidor=input("Distribuidor: "),
        precio=float(input("Precio: $"))
    )

def capturar_medicamento():
    print("\nCapturar Medicamento:")
    return Medicamento(
        nombre=input("Nombre: "),
        distribuidora=input("Distribuidora: "),
        precio=float(input("Precio: $")),
        farmaceutica=input("Farmacéutica: ")
    )

def mostrar_menu():
    print("""  _____ _____ _   _ _____ __  __  ___  ____    _     ___     ___  _   _ _____ 
 |_   _| ____| \ | | ____|  \/  |/ _ \/ ___|  | |   / _ \   / _ \| | | | ____|
   | | |  _| |  \| |  _| | |\/| | | | \___ \  | |  | | | | | | | | | | |  _|  
   | | | |___| |\  | |___| |  | | |_| |___) | | |__| |_| | | |_| | |_| | |___ 
   |_| |_____|_| \_|_____|_|  |_|\___/|____/  |_____\___/   \__\_\\___/|_____|
  _   _ _____ ____ _____ ____ ___ _____  _        ____      _                 
 | \ | | ____/ ___| ____/ ___|_ _|_   _|/ \      / ___|    / \                
 |  \| |  _|| |   |  _| \___ \| |  | | / _ \     \___ \   / _ \               
 | |\  | |__| |___| |___ ___) | |  | |/ ___ \ _   ___) | / ___ \ _            
 |_| \_|_____\____|_____|____/___| |_/_/   \_( ) |____(_)_/   \_(_)           """)
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA DE INVENTARIO ===")
        print("1. Agregar Alimento")
        print("2. Agregar Libro")
        print("3. Agregar Medicamento")
        print("4. Mostrar productos > $10")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            inventario.agregar(capturar_alimento())
        elif opcion == "2":
            inventario.agregar(capturar_libro())
        elif opcion == "3":
            inventario.agregar(capturar_medicamento())
        elif opcion == "4":
            inventario.mostrar_caros()
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

mostrar_menu()
