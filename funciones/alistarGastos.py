import json
from rich.console import Console
from rich.table import Table
from os.path import exists

GASTOS_FILE = "gastos.json"

def cargar_gastos():
    """Carga los gastos y categorías desde un archivo JSON."""
    if exists(GASTOS_FILE):
        with open(GASTOS_FILE, "r") as file:
            return json.load(file)
    return {"gastos": [], "categorias": ["Comida", "Transporte", "Entretenimiento", "Otros"]}

def guardar_gasto(gasto):
    """Guarda un gasto en el archivo JSON."""
    data = cargar_gastos()
    data["gastos"].append(gasto)  # Añadir el nuevo gasto
    with open(GASTOS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def listar_gastos(return_list=False):
    """Carga los gastos desde un archivo JSON y los muestra en una tabla."""
    console = Console()
    data = cargar_gastos()
    gastos = data["gastos"]  # Acceder a los gastos en lugar de directamente a la lista de gastos

    if not gastos:
        console.print("[bold yellow]No hay gastos registrados.[/bold yellow]")
        return [] if return_list else None

    # Crear y mostrar la tabla
    table = Table(title="💰 [bold green]Lista de Gastos[/bold green] 💰", show_lines=True)
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Monto", justify="right", style="magenta")
    table.add_column("Descripción", style="green")
    table.add_column("Categoría", style="blue")
    table.add_column("Fecha y Hora", style="yellow")

    for idx, gasto in enumerate(gastos, start=1):
        table.add_row(
            str(idx),
            f"${gasto['monto']:.2f}",
            gasto['descripcion'],
            gasto['categoria'],
            gasto['fecha_hora']
        )

    console.print(table)
    return gastos if return_list else None

def agregar_categoria(categoria):
    """Agrega una nueva categoría al archivo JSON."""
    data = cargar_gastos()
    if categoria not in data["categorias"]:
        data["categorias"].append(categoria)
        with open(GASTOS_FILE, "w") as file:
            json.dump(data, file, indent=4)
        print(f"\n[green]Categoría '{categoria}' agregada exitosamente.[/green]")
    else:
        print(f"\n[red]La categoría '{categoria}' ya existe.[/red]")

def agregar_gasto():
    """Formulario para agregar un gasto con opción de agregar categorías nuevas."""
    try:
        print("\n[Agregar nuevo gasto]\n")

        # Cargar las categorías del archivo JSON
        data = cargar_gastos()  # Cargar los datos
        categorias = data["categorias"]  # Acceder correctamente a las categorías
        print("\nSelecciona una categoría existente o presiona 'a' para agregar una nueva:")
        for idx, cat in enumerate(categorias, start=1):
            print(f"{idx}. {cat}")
        print(f"{len(categorias) + 1}. Agregar nueva categoría")

        # Opción de elegir categoría o agregar una nueva
        cat_index = input("Categoría [1-4] o 'a' para agregar nueva: ").strip()

        if cat_index.lower() == 'a':  # Opción para agregar una nueva categoría
            nueva_categoria = input("Ingresa el nombre de la nueva categoría: ").strip()
            if nueva_categoria:
                agregar_categoria(nueva_categoria)
                categoria = nueva_categoria
            else:
                print("\n[red]Nombre de categoría inválido. Operación cancelada.[/red]")
                return
        elif not cat_index.isdigit() or int(cat_index) not in range(1, len(categorias) + 1):
            print("\n[red]Categoría inválida. Operación cancelada.[/red]")
            return
        else:
            categoria = categorias[int(cat_index) - 1]  # Correcta asignación de la categoría

        # Captura de la descripción
        descripcion = input("Descripción del gasto: ").strip()
        if not descripcion:
            print("\n[red]Descripción vacía. Operación cancelada.[/red]")
            return

        # Captura del monto
        monto = input("Monto del gasto ($): ").strip()
        if not monto or not monto.replace(".", "", 1).isdigit():
            print("\n[red]Monto inválido. Operación cancelada.[/red]")
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
        print("\n[green]¡Gasto agregado exitosamente![/green]")
        print(f"Monto: ${monto}")
        print(f"Descripción: {descripcion}")
        print(f"Categoría: {categoria}")
        print(f"Fecha y hora: {fecha_hora}")

    except Exception as e:
        print(f"\n[red]Ocurrió un error: {e}[/red]")

if __name__ == "__main__":
    agregar_gasto()
