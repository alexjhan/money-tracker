from menu import show_menu
from funciones.alistarGastos import listar_gastos
from funciones.bagregarGasto import agregar_gasto
from funciones.celiminarGasto import eliminar_gasto
from funciones.dmodificarGasto import modificar_gasto
from funciones.elistarCategorias import listar_categorias
from limpiezaDePantalla import clear_screen

def main():
    while True:
        show_menu()
        option = input("Ingrese una opción: ")
        if option == "1": #listar gastos
            print("1")
            clear_screen()
            listar_gastos()
        elif option == "2": #agregar gasto
            print("2")
            clear_screen()
            agregar_gasto()
        elif option == "3": #eliminar gasto
            print("3")
            clear_screen()
            eliminar_gasto()
        elif option == "4": #modificar gasto
            clear_screen()
            print("4")
            modificar_gasto()
        elif option == "5": #listar categorías
            print("5")
            listar_categorias()
        elif option == "6": #salir
            print("Gracias por usar el sistema de gestión de gastos")
            break
        else:
            print("Opción inválida ingrese de nuevo")
if __name__ == "__main__":
    main()