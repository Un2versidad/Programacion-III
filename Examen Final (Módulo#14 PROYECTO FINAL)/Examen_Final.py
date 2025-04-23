# Hecho por: Franklin Leon, Usando Pycharm, Recomendable Compilarlo con Collab para evitar problemas con las librerias o mejor en un IDE Local.
import json
import os
import logging
import importlib.util
import sys
from typing import Any

# Función para verificar si un módulo está instalado, de lo contrario, se detiene el programa
def verificar_dependencia(modulo: str, paquete: str = None):
    if importlib.util.find_spec(modulo) is None:
        print(f"[bold red]¡Error! No se encontró el módulo '{paquete or modulo}'.[/bold red]")
        print(f"Instálalo con: pip install {paquete or modulo}")
        print("Sugerencia: Usa Google Colab (https://colab.research.google.com/) para un entorno con 'rich' preinstalado.")
        print("Alternativa: Configura un entorno local con Python 3.8+ y usa un IDE como PyCharm, VS Code o IDLE.")
        sys.exit(1)

# Verificación inicial del módulo 'rich'
verificar_dependencia("rich")

# Importación de componentes de la librería 'rich' para la interfaz de consola
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, Confirm

# Verifica si la versión de Python es compatible
def verificar_compatibilidad():
    if sys.version_info < (3, 8):
        print("[bold red]Error: Este programa requiere Python 3.8 o superior ❌[/bold red]")
        print("Tu versión actual es:", sys.version)
        print("Sugerencia: Usa Google Colab para ejecutar este código en un entorno compatible.")
        print("Alternativa: Instala Python 3.8+ localmente o usa un IDE como PyCharm, VS Code o IDLE.")
        sys.exit(1)
    try:
        from rich import print as rprint
        rprint("[bold green]Entorno compatible detectado ✔️[/bold green]")
    except ImportError:
        print("[bold red]Error: El entorno no soporta la librería 'rich'.[/bold red]")
        sys.exit(1)

verificar_compatibilidad()

# Configuración del sistema de logs
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("biblioteca.log", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
logger.addHandler(file_handler)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL + 1)
logger.addHandler(console_handler)

# Archivo donde se guarda el catálogo
ARCHIVO_JSON = "catalogo.json"

# Diccionario con la configuración de cada tipo de material
MATERIALES = {
    "1": {"nombre": "Libro", "clase": "Libro", "campo": "numero_paginas", "prompt": "Número de páginas", "tipo": int},
    "2": {"nombre": "Revista", "clase": "Revista", "campo": "numero_edicion", "prompt": "Número de edición", "tipo": str},
    "3": {"nombre": "DVD", "clase": "DVD", "campo": "duracion", "prompt": "Duración (minutos)", "tipo": int}
}

console = Console()

# Clase base para todos los materiales
class MaterialBiblioteca:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_informacion(self):
        # Muestra los datos básicos
        console.print(f"Título: {self.titulo}")
        console.print(f"Autor: {self.autor}")
        console.print(f"Año: {self.anio_publicacion}")

    def to_dict(self):
        # Convierte el objeto a un diccionario para poder guardarlo
        return {
            'tipo': self.__class__.__name__,
            'titulo': self.titulo,
            'autor': self.autor,
            'anio_publicacion': self.anio_publicacion
        }

# Subclase para libros
class Libro(MaterialBiblioteca):
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, numero_paginas: int):
        super().__init__(titulo, autor, anio_publicacion)
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        console.print(f"Páginas: {self.numero_paginas}")

    def to_dict(self):
        data = super().to_dict()
        data['numero_paginas'] = self.numero_paginas
        return data

# Subclase para revistas
class Revista(MaterialBiblioteca):
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, numero_edicion: str):
        super().__init__(titulo, autor, anio_publicacion)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        console.print(f"Edición: {self.numero_edicion}")

    def to_dict(self):
        data = super().to_dict()
        data["numero_edicion"] = self.numero_edicion
        return data

# Subclase para DVD
class DVD(MaterialBiblioteca):
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, duracion: int):
        super().__init__(titulo, autor, anio_publicacion)
        self.duracion = duracion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        console.print(f"Duración: {self.duracion} minutos")

    def to_dict(self):
        data = super().to_dict()
        data['duracion'] = self.duracion
        return data

# Clase principal de la biblioteca
class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.cargar_de_json()

    # Añade un nuevo material al catálogo
    def agregar_material(self):
        console.print("\n[bold cyan]¡Añadir algo nuevo al catálogo![/bold cyan]")
        for k, v in MATERIALES.items():
            console.print(f"[{k}] {v['nombre']}")
        tipo = Prompt.ask("¿Qué tipo?", choices=list(MATERIALES.keys()))
        info = MATERIALES[tipo]
        try:
            titulo = Prompt.ask("Título")
            autor = Prompt.ask("Autor")
            anio = IntPrompt.ask("Año de publicación / Ejemplo:", default=2023)
            if anio < 0 or anio > 2025:
                raise ValueError("Año no válido")
            extra = Prompt.ask(info["prompt"])
            extra = info["tipo"](extra) if info["tipo"] == int else extra
            if info["tipo"] == int and extra <= 0:
                raise ValueError(f"{info['prompt']} debe ser mayor a 0")

            # Verifica si ya existe un material idéntico y lo reemplaza
            material = globals()[info["clase"]](titulo, autor, anio, extra)
            campo = info["campo"]
            for i, existing in enumerate(self.catalogo):
                if (existing.__class__.__name__ == info["clase"] and
                        existing.titulo == titulo and
                        existing.autor == autor and
                        existing.anio_publicacion == anio and
                        getattr(existing, campo) == extra):
                    self.catalogo[i] = material
                    console.print("[bold yellow]Material idéntico encontrado. Se reemplazó el existente.[/bold yellow]")
                    self.guardar_en_json()
                    logger.info(f"Reemplazado {info['nombre']}: {titulo}")
                    return

            self.catalogo.append(material)
            self.guardar_en_json()
            console.print("[bold green]¡Agregado con éxito![/bold green]")
            logger.info(f"Nuevo {info['nombre']}: {titulo}")
        except ValueError as e:
            console.print(f"[bold red]Error: {e}[/bold red]")

    # Muestra todos los materiales en formato tabla
    def listar_materiales(self):
        if not self.catalogo:
            console.print("[yellow]El catálogo está vacío.[/yellow]")
            return
        tabla = Table(title="Catálogo de la Biblioteca", header_style="bold magenta")
        tabla.add_column("ID")
        tabla.add_column("Tipo")
        tabla.add_column("Título")
        tabla.add_column("Autor")
        tabla.add_column("Año")
        tabla.add_column("Detalles")
        for i, item in enumerate(self.catalogo, 1):
            tipo = item.__class__.__name__
            detalles = (
                f"Páginas: {item.numero_paginas}" if tipo == "Libro" else
                f"Edición: {item.numero_edicion}" if tipo == "Revista" else
                f"Duración: {item.duracion} min"
            )
            tabla.add_row(str(i), tipo, item.titulo, item.autor, str(item.anio_publicacion), detalles)
        console.print(tabla)

    # Permite buscar materiales por título
    def buscar_material(self):
        titulo = Prompt.ask("¿Qué título buscas?")
        encontrados = [item for item in self.catalogo if titulo.lower() in item.titulo.lower()]
        if not encontrados:
            console.print("[yellow]No encontró algún material con ese título.[/yellow]")
            return

        if len(encontrados) == 1:
            console.print("\n[bold cyan]¡Encontré esto![/bold cyan]")
            encontrados[0].mostrar_informacion()
        else:
            console.print(f"\n[bold cyan]Encontré {len(encontrados)} resultados:[/bold cyan]")
            tabla = Table(header_style="bold magenta")
            tabla.add_column("ID")
            tabla.add_column("Tipo")
            tabla.add_column("Título")
            tabla.add_column("Autor")
            tabla.add_column("Año")
            tabla.add_column("Detalles")
            for i, item in enumerate(encontrados, 1):
                tipo = item.__class__.__name__
                detalles = (
                    f"Páginas: {item.numero_paginas}" if tipo == "Libro" else
                    f"Edición: {item.numero_edicion}" if tipo == "Revista" else
                    f"Duración: {item.duracion} min"
                )
                tabla.add_row(str(i), tipo, item.titulo, item.autor, str(item.anio_publicacion), detalles)
            console.print(tabla)

            seleccion = IntPrompt.ask("Selecciona el ID del material para ver detalles", default=1,choices=[str(i) for i in range(1, len(encontrados) + 1)])
            console.print("\n[bold cyan]Detalles del material seleccionado:[/bold cyan]")
            encontrados[seleccion - 1].mostrar_informacion()

    # Elimina un material del catálogo
    def eliminar_material(self):
        titulo = Prompt.ask("Título del material que quieres eliminar?")
        encontrados = [item for item in self.catalogo if titulo.lower() in item.titulo.lower()]
        if not encontrados:
            console.print("[yellow]No se encontró algún material con ese título.[/yellow]")
            return
        if len(encontrados) == 1:
            item = encontrados[0]
            if Confirm.ask(f"¿Seguro que deseas eliminar '{item.titulo}' de {item.__class__.__name__}?"):
                self.catalogo.remove(item)
                self.guardar_en_json()
                console.print("[bold green]Material eliminado con éxito.[/bold green]")
                logger.info(f"Eliminado: {item.titulo}")
        else:
            console.print(f"[bold cyan]Se encontraron varios materiales llamados '{titulo}':[/bold cyan]")
            tabla = Table(title="Selecciona qué eliminar", header_style="bold magenta")
            tabla.add_column("ID")
            tabla.add_column("Tipo")
            tabla.add_column("Título")
            tabla.add_column("Autor")
            tabla.add_column("Año")
            tabla.add_column("Detalles")
            for i, item in enumerate(encontrados, 1):
                tipo = item.__class__.__name__
                detalles = (
                    f"Páginas: {item.numero_paginas}" if tipo == "Libro" else
                    f"Edición: {item.numero_edicion}" if tipo == "Revista" else
                    f"Duración: {item.duracion} min"
                )
                tabla.add_row(str(i), tipo, item.titulo, item.autor, str(item.anio_publicacion), detalles)
            console.print(tabla)
            seleccion = IntPrompt.ask("Selecciona el ID del material a eliminar", choices=[str(i) for i in range(1, len(encontrados)+1)])
            seleccionado = encontrados[seleccion - 1]
            if Confirm.ask(f"¿Estás seguro que deseas eliminar '{seleccionado.titulo}'?"):
                self.catalogo.remove(seleccionado)
                self.guardar_en_json()
                console.print("[bold green]Material eliminado con éxito.[/bold green]")
                logger.info(f"Eliminado: {seleccionado.titulo}")

    # Guarda el catálogo actual en un archivo JSON
    def guardar_en_json(self):
        try:
            with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
                archivo_tipeado: Any = archivo
                json.dump([item.to_dict() for item in self.catalogo], archivo_tipeado, indent=4, ensure_ascii=False)
            logger.info("Catálogo guardado")
        except Exception as e:
            console.print(f"[bold red]No pude guardar: {e}[/bold red]")

    # Carga los datos del catálogo desde un archivo JSON
    def cargar_de_json(self):
        if not os.path.exists(ARCHIVO_JSON):
            return
        try:
            with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    tipo = item["tipo"]
                    if tipo in ["Libro", "Revista", "DVD"]:
                        campo = MATERIALES[str([k for k, v in MATERIALES.items() if v["clase"] == tipo][0])]["campo"]
                        material = globals()[tipo](item["titulo"], item["autor"], item["anio_publicacion"], item[campo])
                        self.catalogo.append(material)
            logger.info(f"Cargué {len(self.catalogo)} items")
        except Exception as e:
            console.print(f"[bold red]Error al cargar catálogo: {e}[/bold red]")

    # Muestra el menú principal de interacción
    def mostrar_menu(self):
        console.print("[bold green]¡Bienvenido a la Biblioteca! 📚[/bold green]")
        while True:
            console.print(Panel(
                "[1] Añadir material\n[2] Ver catálogo\n[3] Buscar por título\n[4] Eliminar material\n[5] Salir",
                title="Menú Principal", border_style="bold blue"
            ))
            opcion = Prompt.ask("Elige una opción", choices=["1", "2", "3", "4", "5"])
            if opcion == "1":
                self.agregar_material()
            elif opcion == "2":
                self.listar_materiales()
            elif opcion == "3":
                self.buscar_material()
            elif opcion == "4":
                self.eliminar_material()
            elif opcion == "5":
                if Confirm.ask("¿Seguro que quieres salir?"):
                    console.print("[bold green]¡Nos vemos! 😄[/bold green]")
                    break

# Inicializa el sistema
logger.info("Sistema arrancado")
biblioteca = Biblioteca()
biblioteca.mostrar_menu()