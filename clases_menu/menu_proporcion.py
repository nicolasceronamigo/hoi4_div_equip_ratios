from clases_menu.menu import Menu


class MenuProporcion(Menu):
    def calcular_proporcion(self):
        costos_totales = {}
        proporcion_costo = {}
        for fila in self.get_tabla().get_matriz():
            if fila["id"] != "id":
                costos_totales[fila["id"]] = float(fila["costo/uni"]) * int(fila["cant"])
        costo_total_min = min(costos_totales.values())
        for id in costos_totales.keys():
            proporcion_costo[id] = costos_totales[id] / costo_total_min
            print(f"| {id} | {proporcion_costo[id]} |")
        return True
        