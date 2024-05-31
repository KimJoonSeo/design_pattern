from abc import ABC

from abstract_factory_pattern.pizza_ingredient_factory import PizzaIngredientFactory


class Pizza(ABC):
    name: str
    dough: str
    sauce: str

    def prepare(self) -> None:
        print("Prepare")

    def bake(self) -> None:
        print("Bake")

    def cut(self) -> None:
        print("Cut")

    def box(self) -> None:
        print("Box")

    def get_name(self) -> str:
        return self.name

    def set_name(self, name) -> None:
        self.name = name


class CheesePizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Prepare")
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_dough()
        print(str(dough) + '\n' + str(sauce))


class VeggiePizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Prepare")
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_dough()
        print(str(dough) + '\n' + str(sauce))
