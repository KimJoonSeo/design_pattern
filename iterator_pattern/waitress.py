from typing import List

from iterator_pattern.menus import Menu, MenuItem


class Waitress:
    menus: List[Menu]
    def __init__(self, menus: List[Menu]):
        self.menus = menus

    def _print_menu(self, iter_menu: Menu):
        for menu_item in iter_menu:
            menu_item: MenuItem
            print(f"{menu_item.name}, {menu_item.price} -- {menu_item.description}")

    def print_menu(self):
        for menu in self.menus:
            print("-----print menu-----")
            self._print_menu(menu)

    def _is_vegetarian(self, name, iter_menu: Menu):
        for menu_item in iter_menu:
            menu_item: MenuItem
            if menu_item.name == name:
                return menu_item.is_vegetarian
        return False

    def is_item_vegetarian(self, name):
        for menu in self.menus:
            if self._is_vegetarian(name, menu):
                return True
        return False
