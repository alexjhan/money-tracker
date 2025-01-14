from rich.console import Console
from rich.prompt import Prompt
from funciones.alistarGastos import listar_gastos  # Asegúrate de que esta función esté importada correctamente
from limpiezaDePantalla import clear_screen
import json
from os.path import exists

GASTOS_FILE = "gastos.json"

def modificar_gasto():
    """Modifica un gasto existente en el archivo JSON, con la opción de salir en cualquier momento."""
    console = Console()

    # Cargar los datos del archivo JSON
    if exists(GASTOS_FILE):
        with open(GASTOS_FILE, "r") as file:
            data = json.load(file)
        gastos = data["gastos"]  # Acceder a los gastos dentro de la estructura del JSON
    else:
        gastos = []

    if not gastos:
        console.print("[bold yellow]No hay gastos disponibles para modificar.[/bold yellow]")
        return

    # Mostrar la tabla de gastos
    listar_gastos(gastos)  # Asegúrate de que esta función esté bien definida en otro archivo
    console.print("[bold cyan]Escriba 'salir' en cualquier momento para cancelar.[/bold cyan]")

    try:
        # Solicitar el ID del gasto a modificar
        gasto_id = Prompt.ask(
            "[bold cyan]Ingrese el ID del gasto a modificar[/bold cyan]",
            choices=[str(i) for i in range(1, len(gastos) + 1)] + ["salir"]
        )
        
        if gasto_id.lower() == "salir":
            console.print("[bold yellow]Operación cancelada por el usuario.[/bold yellow]")
            clear_screen()
            return

        gasto_id = int(gasto_id) - 1  # Convertir a índice basado en 0
        gasto_a_modificar = gastos[gasto_id]
        console.print(
            f"[bold blue]Gasto seleccionado:[/bold blue] "
            f"[yellow]{gasto_a_modificar['descripcion']} - ${gasto_a_modificar['monto']:.2f}[/yellow]"
        )

        # Solicitar nuevos valores para cada campo
        nuevo_monto = Prompt.ask(
            f"[bold green]Nuevo monto[/bold green] (actual: ${gasto_a_modificar['monto']:.2f})",
            default=str(gasto_a_modificar['monto'])
        )
        if nuevo_monto.lower() == "salir":
            console.print("[bold yellow]Operación cancelada por el usuario.[/bold yellow]")
            clear_screen()
            return

        nueva_descripcion = Prompt.ask(
            f"[bold green]Nueva descripción[/bold green] (actual: {gasto_a_modificar['descripcion']})",
            default=gasto_a_modificar['descripcion']
        )
        if nueva_descripcion.lower() == "salir":
            console.print("[bold yellow]Operación cancelada por el usuario.[/bold yellow]")
            clear_screen()
            return

        # Obtener las categorías existentes
        categorias_existentes = {gasto["categoria"] for gasto in gastos if "categoria" in gasto}

        # Preguntar por la nueva categoría
        nueva_categoria = Prompt.ask(
            f"[bold green]Nueva categoría[/bold green] (actual: {gasto_a_modificar['categoria']})\n"
            f"[cyan]Seleccione una categoría existente o ingrese una nueva. (Escriba 'salir' para cancelar)[/cyan]",
            default=gasto_a_modificar['categoria'],
            choices=["salir"] + list(categorias_existentes) + ["nueva categoría"]
        )

        if nueva_categoria.lower() == "salir":
            console.print("[bold yellow]Operación cancelada por el usuario.[/bold yellow]")
            clear_screen()
            return

        if nueva_categoria.lower() == "nueva categoría":
            nueva_categoria = Prompt.ask("[bold green]Ingrese la nueva categoría:[/bold green]")

        # Actualizar los valores del gasto
        gasto_a_modificar['monto'] = float(nuevo_monto)
        gasto_a_modificar['descripcion'] = nueva_descripcion
        gasto_a_modificar['categoria'] = nueva_categoria

        # Guardar los cambios en el archivo JSON
        data["gastos"] = gastos  # Asegurarse de que los gastos se actualicen correctamente
        with open(GASTOS_FILE, "w") as file:
            json.dump(data, file, indent=4)

        console.print("[bold green]Gasto modificado exitosamente.[/bold green]")

    except ValueError:
        console.print("[bold red]Entrada inválida. Por favor, intente nuevamente.[/bold red]")
    except IndexError:
        console.print("[bold red]ID inválido. Intente nuevamente.[/bold red]")
