from rich.console import Console
from rich.table import Table
import json
from os.path import exists

GASTOS_FILE = "gastos.json"

def listar_categorias():
    """Lista todas las categorías únicas de los gastos."""
    console = Console()

    # Verificar si el archivo de gastos existe
    if not exists(GASTOS_FILE):
        console.print("[bold red]El archivo de gastos no existe. No hay categorías para mostrar.[/bold red]")
        return

    # Cargar los gastos desde el archivo JSON
    with open(GASTOS_FILE, "r") as file:
        data = json.load(file)

    # Asegurarse de que los datos contengan la clave "gastos" si es una estructura con esa clave
    gastos = data.get("gastos", []) if isinstance(data, dict) else data

    # Obtener todas las categorías únicas
    categorias = {gasto["categoria"] for gasto in gastos if "categoria" in gasto}

    if not categorias:
        console.print("[bold yellow]No hay categorías disponibles para listar.[/bold yellow]")
        return

    # Mostrar las categorías en una tabla
    table = Table(title="📂 [bold cyan]Categorías de Gastos[/bold cyan]")
    table.add_column("ID", justify="center", style="green")
    table.add_column("Categoría", style="magenta")

    for idx, categoria in enumerate(sorted(categorias), start=1):
        table.add_row(str(idx), categoria)

    console.print(table)
