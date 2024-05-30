from abc import ABC, abstractmethod
from typing import Optional

from factory_method_pattern.pizza import Pizza, \
    ChicagoStyleCheesePizza, ChicagoStyleVeggiePizza, \
    NYStyleCheesePizza, NYStylePepperoniPizza


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


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type) -> Optional[Pizza]:
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza()
        elif pizza_type == 'veggie':
            return ChicagoStyleVeggiePizza()
        return None


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type) -> Optional[Pizza]:
        if pizza_type == 'cheese':
            return NYStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            return NYStylePepperoniPizza()
        return None
