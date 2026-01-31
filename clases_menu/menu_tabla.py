from clases_menu.menu import Menu


class MenuTabla(Menu):
    def mostrar_tabla(self):
        print(self.get_tabla().mostrar_tabla())
        return True