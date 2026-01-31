from clases_tabla.tabla import Tabla
from clases_menu.menu import Menu
from clases_menu.menu_filas import  MenuFilas
from clases_menu.menu_proporcion import MenuProporcion
from clases_menu.menu_tabla import MenuTabla


tabla1 = Tabla("División Infantería", {"nombre": "nombre", "costo/uni": "costo/uni", "cant": "cant"})

menu_principal = Menu("División Infantería, proporción de fábricas", tabla1)
menu_filas = MenuFilas("Editar Filas", tabla1)
menu_proporcion = MenuProporcion("Calcular Proporción", tabla1)
menu_tabla = MenuTabla("Tabla", tabla1)

menu_principal.agregar_opcion(0, "Salir", menu_principal.salir)
menu_principal.agregar_opcion(1, "Editar Filas", menu_filas.ciclo_menu)
menu_principal.agregar_opcion(2, "Calcular Proporción", menu_proporcion.calcular_proporcion)
menu_principal.agregar_opcion(3, "Mostrar Tabla", menu_tabla.ciclo_menu)

menu_filas.agregar_opcion(0, "Salir", menu_filas.salir)
menu_filas.agregar_opcion(1, "Crear Fila", menu_filas.crear_fila)
menu_filas.agregar_opcion(2, "Mostrar Fila", menu_filas.mostrar_fila)
menu_filas.agregar_opcion(3, "Modificar Fila", menu_filas.modificar_valor_fila)
menu_filas.agregar_opcion(4, "Eliminar Fila", menu_filas.eliminar_fila)

menu_tabla.agregar_opcion(0, "Salir", menu_tabla.salir)
menu_tabla.agregar_opcion(1, "Mostrar Tabla", menu_tabla.mostrar_tabla)

menu_principal.ciclo_menu()