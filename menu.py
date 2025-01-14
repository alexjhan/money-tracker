from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns

def show_menu():
    console = Console() 
    table = Table(title="⭐ [bold yellow]Elige una opción.[/bold yellow]")
    table.add_column("Opción", justify="center", style="cyan", no_wrap=True)
    table.add_column("Descripción", style="bold cyan")
    table.add_row("1", "Listar gastos")
    table.add_row("2", "Agregar gasto")
    table.add_row("3", "Eliminar gasto")
    table.add_row("4", "Modificar gasto")
    table.add_row("5", "Listar categorías")
    table.add_row("6", "Salir")
    menu_panel = Panel(table,title="📋 [bold magenta]MENÚ[/bold magenta]", border_style="white",expand=False)
       
     # Crear las estadísticas
    stats_content = """
    📊 [bold yellow]Estadísticas actuales[/bold yellow]
    Total de gastos: [bold cyan]$1230.45[/bold cyan]
    Categorías: [bold cyan]5[/bold cyan]
    Gasto promedio: [bold cyan]$205.07[/bold cyan]
    Último gasto: [bold cyan]$50 en comida[/bold cyan]
    """
    stats_panel = Panel(stats_content, title="📊 [bold magenta]RESUMEN[/bold magenta]", border_style="white")
    console.print(Columns([menu_panel, stats_panel], align="center"))

