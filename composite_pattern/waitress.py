from composite_pattern.menu_component import MenuComponent


class Waitress:
    all_menus: MenuComponent

    def __init__(self, all_menus: MenuComponent):
        self.all_menus = all_menus

    def print_menu(self):
        self.all_menus.print()