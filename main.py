from menu import show_menu
from funciones.alistarGastos import listar_gastos
from funciones.bagregarGasto import agregar_gasto
from funciones.celiminarGasto import eliminar_gasto
from funciones.dmodificarGasto import modificar_gasto
from funciones.elistarCategorias import listar_categorias
from funciones.fagregarCategoria import agregar_categoria

def main():
    while True:
        show_menu()
        option = input("Ingrese una opción: ")
        if option == "1": #listar gastos
            print("1")
            listar_gastos()
        elif option == "2": #agregar gasto
            print("2")
            agregar_gasto()
        elif option == "3": #eliminar gasto
            print("3")
            eliminar_gasto()
        elif option == "4": #modificar gasto
            print("4")
            modificar_gasto()
        elif option == "5": #listar categorías
            print("5")
            listar_categorias()
        elif option == "6": #agregar categoría
            print("6")
            agregar_categoria()
        elif option == "7": #salir
            print("Gracias por usar el sistema de gestión de gastos")
            break
        else:
            print("Opción inválida ingrese de nuevo")
if __name__ == "__main__":
    main()