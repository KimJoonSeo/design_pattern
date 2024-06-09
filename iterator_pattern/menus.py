from abc import ABC, abstractmethod


class MenuItem:
    name: str
    description: str
    is_vegetarian: bool
    price: float

    def __init__(self, name, description, is_vegetarian, price):
        self.name = name
        self.description = description
        self.is_vegetarian = is_vegetarian
        self.price = price


class Menu(ABC):
    @abstractmethod
    def __iter__(self):
        pass


class CafeMenu(Menu):
    menu_items: dict

    def __init__(self):
        self.menu_items = {}
        self.add_item(
            "Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            True,
            3.99,
        )
        self.add_item(
            "Soup of the day",
            "A cup of the soup of the day, with a side salad",
            False,
            3.69,
        )
        self.add_item(
            "Burrito",
            "A large burrito, with whole pinto beans, salsa, guacamole",
            True,
            4.29,
        )

    def add_item(self, name: str, description: str, is_vegetarian: bool, price: float):
        self.menu_items[name] = MenuItem(name, description, is_vegetarian, price)

    def __iter__(self):
        return iter(self.menu_items.values())

class DinerMenu(Menu):
    menu_items: list

    def __init__(self):
        self.menu_items = []
        self.add_item(
            "Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat",
            True,
            2.99,
        )
        self.add_item("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.add_item(
            "Soup of the day",
            "Soup of the day, with a side of potato salad",
            False,
            3.29,
        )
        self.add_item(
            "Hotdog",
            "A hot dog, with sauerkraut, relish, onions, topped with cheese",
            False,
            3.05,
        )
        self.add_item(
            "Steamed Veggies and Brown Rice",
            "A medly of steamed vegetables over brown rice",
            True,
            3.99,
        )
        self.add_item(
            "Pasta",
            "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
            True,
            3.89,
        )
    def add_item(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float,
    ):
        self.menu_items.append(MenuItem(name, description, vegetarian, price))

    def __iter__(self):
        return iter(self.menu_items)

class PancakeHouseMenu(Menu):
    menu_items: set

    def add_item(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float,
    ):
        self.menu_items.add(MenuItem(name, description, vegetarian, price))
    def __init__(self):
        self.menu_items = set()

        self.add_item("K&B's Pancake Breakfast",
                "Pancakes with scrambled eggs and toast",
                True,
                2.99)

        self.add_item("Regular Pancake Breakfast",
                "Pancakes with fried eggs, sausage",
                False,
                2.99)

        self.add_item("Blueberry Pancakes",
                "Pancakes made with fresh blueberries and blueberry syrup",
                True,
                3.49)

        self.add_item("Waffles",
                "Waffles with your choice of blueberries or strawberries",
                True,
                3.59)


    def __iter__(self):
        return iter(self.menu_items)