from prompt_toolkit.shortcuts.dialogs import input_dialog, radiolist_dialog
from prompt_toolkit.styles import Style

def agregar_gasto():
    # Estilo para personalizar los diálogos
    style = Style.from_dict({
        "dialog": "bg:#2c3e50 #ffffff",
        "input-field": "bg:#34495e #ffffff",
        "button": "bg:#16a085",
        "dialog.body": "bg:#2c3e50 #ffffff",
        "dialog.title": "bg:#2980b9 #ffffff",
    })
    
    # Obtener el monto del gasto
    monto = input_dialog(
        title="Agregar Gasto",
        text="Ingresa el monto del gasto:",
        style=style
    ).run()

    # Si el usuario cancela
    if monto is None:
        return

    # Obtener la descripción
    descripcion = input_dialog(
        title="Descripción del Gasto",
        text="Ingresa una descripción:",
        style=style
    ).run()

    if descripcion is None:
        return

    # Seleccionar la categoría usando opciones
    categoria = radiolist_dialog(
        title="Selecciona una Categoría",
        text="Selecciona la categoría del gasto:",
        values=[
            ("comida", "Comida"),
            ("transporte", "Transporte"),
            ("entretenimiento", "Entretenimiento"),
            ("otros", "Otros"),
        ],
        style=style
    ).run()

    if categoria is None:
        return

    # Confirmar y mostrar los resultados
    print("\n[bold cyan]Gasto agregado exitosamente:[/bold cyan]")
    print(f"Monto: ${monto}")
    print(f"Descripción: {descripcion}")
    print(f"Categoría: {categoria}")

# Ejecutar
if __name__ == "__main__":
    agregar_gasto()
