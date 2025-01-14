from prompt_toolkit import prompt
from datetime import datetime
import json
from os.path import exists
from rich.console import Console
from rich import print  # Para los colores
from limpiezaDePantalla import clear_screen
# Archivo JSON donde se guardarán los gastos
GASTOS_FILE = "gastos.json"
console = Console()

def cargar_gastos():
    """Carga los gastos y categorías desde un archivo JSON."""
    if exists(GASTOS_FILE):
        with open(GASTOS_FILE, "r") as file:
            return json.load(file)
    return {"gastos": [], "categorias": ["Comida", "Transporte", "Entretenimiento", "Otros"]}

def guardar_gasto(gasto):
    """Guarda un gasto en el archivo JSON."""
    data = cargar_gastos()
    data["gastos"].append(gasto)
    with open(GASTOS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def agregar_categoria(categoria):
    """Agrega una nueva categoría al archivo JSON."""
    data = cargar_gastos()
    if categoria not in data["categorias"]:
        data["categorias"].append(categoria)
        with open(GASTOS_FILE, "w") as file:
            json.dump(data, file, indent=4)
        console.print(f"\n[green]Categoría '{categoria}' agregada exitosamente.[/green]")
    else:
        console.print(f"\n[red]La categoría '{categoria}' ya existe.[/red]")

def agregar_gasto():
    """Formulario para agregar un gasto con opción de agregar categorías nuevas."""
    try:
        print("\n[bold cyan]Agregar nuevo gasto[/bold cyan]\n")

        # Selección de la categoría
        data = cargar_gastos()  # Cargar los datos
        categorias = data["categorias"]  # Acceder correctamente a las categorías
        print("\n[bold yellow]Selecciona una categoría existente o presiona 'a' para agregar una nueva:[/bold yellow]")
        for idx, cat in enumerate(categorias, start=1):
            print(f"{idx}. {cat}")
        print(f"{len(categorias) + 1}. Agregar nueva categoría")
        print("[bold magenta]Escribe 'salir' en cualquier momento para cancelar.[/bold magenta]")

        # Opción de elegir categoría o agregar una nueva
        cat_index = prompt("Categoría [1-4] o 'a' para agregar nueva: ").strip()

        if cat_index.lower() == 'salir':  # Opción para salir
            clear_screen()
            console.print("[yellow]Operación cancelada por el usuario.[/yellow]")
            return

        if cat_index.lower() == 'a':  # Opción para agregar una nueva categoría
            nueva_categoria = prompt("Ingresa el nombre de la nueva categoría: ").strip()
            if nueva_categoria:
                agregar_categoria(nueva_categoria)
                categoria = nueva_categoria
            else:
                clear_screen()
                console.print("\n[red]Nombre de categoría inválido. Operación cancelada.[/red]")
                return
        elif not cat_index.isdigit() or int(cat_index) not in range(1, len(categorias) + 1):
            clear_screen()
            console.print("\n[red]Categoría inválida. Operación cancelada.[/red]")
            return
        else:
            categoria = categorias[int(cat_index) - 1]

        # Captura de la descripción
        descripcion = prompt("Descripción del gasto: ").strip()
        if not descripcion:
            clear_screen()
            console.print("\n[red]Descripción vacía. Operación cancelada.[/red]")
            return

        # Captura del monto
        monto = prompt("Monto del gasto ($): ").strip()
        if not monto or not monto.replace(".", "", 1).isdigit():
            clear_screen()
            console.print("\n[red]Monto inválido. Operación cancelada.[/red]")
            return

        # Captura automática de la fecha y hora
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Crear el objeto gasto
        gasto = {
            "monto": float(monto),
            "descripcion": descripcion,
            "categoria": categoria,
            "fecha_hora": fecha_hora,
        }

        # Guardar el gasto en JSON
        guardar_gasto(gasto)

        # Confirmar operación
        console.print("\n[green]¡Gasto agregado exitosamente![/green]")
        console.print(f"[bold cyan]Monto:[/bold cyan] ${monto}")
        console.print(f"[bold cyan]Descripción:[/bold cyan] {descripcion}")
        console.print(f"[bold cyan]Categoría:[/bold cyan] {categoria}")
        console.print(f"[bold cyan]Fecha y hora:[/bold cyan] {fecha_hora}")

    except Exception as e:
        clear_screen()
        console.print(f"\n[red]Ocurrió un error: {e}[/red]")

if __name__ == "__main__":
    agregar_gasto()
