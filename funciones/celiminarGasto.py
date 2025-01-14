from rich.console import Console
from rich.prompt import Prompt
import json
from os.path import exists
from funciones.alistarGastos import listar_gastos

GASTOS_FILE = "gastos.json"

def eliminar_gasto():
    """Elimina un gasto del archivo JSON."""
    console = Console()

    # Verificar si el archivo de gastos existe
    if not exists(GASTOS_FILE):
        console.print("[bold red]El archivo de gastos no existe. No hay gastos para eliminar.[/bold red]")
        return

    # Cargar los datos del archivo JSON
    with open(GASTOS_FILE, "r") as file:
        data = json.load(file)

    gastos = data.get("gastos", [])  # Obtener la lista de gastos de la estructura JSON

    if not gastos:
        console.print("[bold yellow]No hay gastos disponibles para eliminar.[/bold yellow]")
        return

    # Mostrar la lista de gastos usando la función listar_gastos
    console.print("[bold cyan]Aquí están los gastos disponibles para eliminar:[/bold cyan]")
    listar_gastos(gastos)  # Asumimos que esta función muestra una tabla de los gastos

    console.print("[bold cyan]Escriba 'salir' en cualquier momento para cancelar.[/bold cyan]")

    # Solicitar al usuario que seleccione un gasto
    try:
        gasto_id = Prompt.ask(
            "[bold cyan]Ingrese el ID del gasto a eliminar o escriba 'salir' para cancelar[/bold cyan]"
        )
        
        if gasto_id.lower() == "salir":
            console.print("[bold yellow]Operación cancelada por el usuario.[/bold yellow]")
            return

        gasto_id = int(gasto_id) - 1  # Convertir a índice basado en 0

        # Confirmar eliminación
        gasto_a_eliminar = gastos[gasto_id]
        confirm = Prompt.ask(
            f"[bold red]¿Está seguro de eliminar el gasto seleccionado?[/bold red] "
            f"[yellow]({gasto_a_eliminar['descripcion']} - ${gasto_a_eliminar['monto']:.2f})[/yellow]",
            choices=["s", "n"],
            default="n"
        )

        if confirm == "s":
            # Eliminar el gasto de la lista
            gastos.pop(gasto_id)

            # Actualizar el archivo JSON con la lista modificada de gastos
            data["gastos"] = gastos
            with open(GASTOS_FILE, "w") as file:
                json.dump(data, file, indent=4)

            console.print("[bold green]Gasto eliminado exitosamente.[/bold green]")
        else:
            console.print("[bold yellow]Eliminación cancelada.[/bold yellow]")

    except ValueError:
        console.print("[bold red]Entrada inválida. Por favor, intente nuevamente.[/bold red]")
    except IndexError:
        console.print("[bold red]ID inválido. Intente nuevamente.[/bold red]")
