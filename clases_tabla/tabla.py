from herramietas.herramientas import igualar_strings_matriz

class Tabla:
    def __init__(self, nombre: str, nombre_columnas: dict[str]):
        self.__nombre = nombre
        nombre_columnas["id"] = "id"
        self.__matriz: list[dict] = [nombre_columnas]
    
    def get_matriz(self):
        return self.__matriz

    def get_fila(self, id: str):
        for fila in self.__matriz:
            if fila["id"] == id:
                return fila

    def ajustar_tabla(self):
        for _ in range(len(self.__matriz)):
            fila = self.__matriz[_]
            nombre_columnas = self.__matriz[0]
            if len(fila) < len(nombre_columnas):
                for key in nombre_columnas.keys():
                    if key not in fila.keys():
                        fila[key] = "-"
            elif len(fila) > len(nombre_columnas): #<-- no se usará en el menú
                for key in fila.keys():
                    if key not in nombre_columnas.keys():
                        nombre_columnas[key] = key
                self.ajustar_tabla()
            
    def agregar_nombre_columna(self, nombre_columna: str):
        self.__matriz[0][nombre_columna] = nombre_columna
        self.ajustar_tabla()
    
    def agregar_fila(self, nueva_fila: dict[str]):
        nuevo_id = "1"
        for fila in self.__matriz:
            if fila["id"] == nuevo_id:
                id_int = int(nuevo_id)
                id_int += 1
                nuevo_id = str(id_int)
        nueva_fila["id"] = str(nuevo_id)
        self.__matriz.append(nueva_fila)
        self.ajustar_tabla()
    
    def modificar_valor_fila(self, id: str, nombre_columna: str, nuevo_valor: str):
        for fila in self.__matriz:
            if fila["id"] == id:
                indice = self.__matriz.index(fila)
                self.__matriz[indice][nombre_columna] = nuevo_valor

    def eliminar_fila(self, id: str):
        for fila in self.__matriz:
            if fila["id"] == id:
                self.__matriz.remove(fila)

    def eliminar_columna(self, nombre_columna: str):
        for fila in self.__matriz:
            fila.pop(nombre_columna)

    def mostrar_tabla(self):
        tabla = f"{self.__nombre}"
        matriz_listas = []
        for fila in self.__matriz:
            fila_lista = []
            for key in fila.keys():
                if key == "id":
                    fila_lista.append(fila[key])
            for key in fila.keys():
                if key != "id":
                    fila_lista.append(fila[key])
            matriz_listas.append(fila_lista)
        matriz_listas_igualada = igualar_strings_matriz(matriz_listas)
        for fila in matriz_listas_igualada:
            tabla += "\n"
            for columna in fila:
                tabla += f"{columna}_|"
        return tabla