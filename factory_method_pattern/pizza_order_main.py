from factory_method_pattern.pizza import Pizza
from factory_method_pattern.pizza_store import PizzaStore, NYPizzaStore, ChicagoPizzaStore


def main():
    ny_store: PizzaStore = NYPizzaStore()
    chicago_store: PizzaStore = ChicagoPizzaStore()

    cheese_pizza: Pizza = ny_store.order_pizza("cheese")
    print(cheese_pizza.get_name())
    print()
    veggie_pizza: Pizza = chicago_store.order_pizza("veggie")
    print(veggie_pizza.get_name())

if __name__ == "__main__":
    main()