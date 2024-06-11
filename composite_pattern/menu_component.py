from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class MenuComponent:
    
    def add(self, component: MenuComponent) -> None:
        raise NotImplementedError

    
    def remove(self, component: MenuComponent) -> None:
        raise NotImplementedError

    
    def get_child(self, i: int) -> MenuComponent:
        raise NotImplementedError

    
    def get_name(self) -> str:
        raise NotImplementedError

    
    def get_description(self) -> str:
        raise NotImplementedError

    
    def get_price(self) -> float:
        raise NotImplementedError

    
    def is_vegetarian(self) -> bool:
        raise NotImplementedError

    
    def print(self) -> None:
        raise NotImplementedError


class MenuItem(MenuComponent):
    name: str
    description: str
    vegetarian: bool
    price: float

    def __init__(self,
                 name: str,
                 description: str,
                 vegetarian: bool,
                 price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def is_vegetarian(self) -> bool:
        return self.vegetarian

    def print(self) -> None:
        print("  " + self.get_name())
        if self.is_vegetarian():
            print("(v)")
        print(", " + str(self.get_price()))
        print("     -- " + self.get_description())

class MenuComposite(MenuComponent):
    menu_components: List[MenuComponent]
    name: str
    description: str

    def __init__(self, name: str, description: str):
        self.menu_components = []
        self.name = name
        self.description = description
    def add(self, component: MenuComponent) -> None:
        self.menu_components.append(component)

    def remove(self, component: MenuComponent) -> None:
        self.menu_components.remove(component)

    def get_child(self, i: int) -> MenuComponent:
        return self.menu_components[i]

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def print(self) -> None:
        print("\n" + self.get_name())
        print(", " + str(self.get_description()))
        print("-------------------------")
        for component in self.menu_components:
            component.print()




