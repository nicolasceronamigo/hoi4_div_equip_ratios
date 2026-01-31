from clases_menu.menu import Menu

class MenuFilas(Menu):
    def crear_fila(self):
        tabla = self.get_tabla()
        nombre_columnas = tabla.get_matriz()[0]
        fila = {}
        for columna in nombre_columnas.keys():
            if columna != "id":
                valor = input(f"Ingrese {columna}: ")
                fila[columna] = valor
        tabla.agregar_fila(fila)
        return True
    
    def mostrar_fila(self):
        id = input("Ingrese el id de la fila a mostrar: ")
        fila = self.get_tabla().get_fila(id)
        print(fila)
        return True
    
    def modificar_valor_fila(self):
        id = input("Ingrese el id de la fila a modificar: ")
        nombre_columna = input("Ingrese el nombre de la columna a modificar: ")
        nuevo_valor = input("Ingrese el nuevo valor: ")
        self.get_tabla().modificar_valor_fila(id, nombre_columna, nuevo_valor)
        return True
    
    def eliminar_fila(self):
        id = input("Ingrese el id de la fila a eliminar: ")
        self.get_tabla().eliminar_fila(id)
        return True