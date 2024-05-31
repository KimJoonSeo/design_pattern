from abc import ABC, abstractmethod
from typing import Optional

from abstract_factory_pattern.pizza import Pizza, VeggiePizza, CheesePizza
from abstract_factory_pattern.pizza_ingredient_factory import PizzaIngredientFactory, NYPizzaIngredientFactory, \
    ChicagoPizzaIngredientFactory


class PizzaStore(ABC):
    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)

        if pizza:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type) -> Optional[Pizza]:
        pass

class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type) -> Optional[Pizza]:
        ingredient_factory: PizzaIngredientFactory = NYPizzaIngredientFactory()
        if pizza_type == 'veggie':
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")
            return pizza
        return None


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type) -> Optional[Pizza]:
        ingredient_factory: PizzaIngredientFactory = ChicagoPizzaIngredientFactory()
        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")
            return pizza
        return None

