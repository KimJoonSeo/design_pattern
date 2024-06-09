from template_method_pattern.caffein_beverage_with_hook import TeaWithHook, CoffeeWithHook, CaffeineBeverageWithHook
from template_method_pattern.caffeine_beverage import Tea, Coffee, CaffeineBeverage


def main():
    tea: CaffeineBeverage = Tea()
    coffee: CaffeineBeverage = Coffee()

    print("\nmaking tea...")
    tea.prepare_recipe()
    print("\nmaking coffee...")
    coffee.prepare_recipe()

    tea_with_hook: CaffeineBeverageWithHook = TeaWithHook()
    coffee_with_hook: CaffeineBeverageWithHook = CoffeeWithHook()

    print("\nmaking tea with hook...")
    tea_with_hook.prepare_recipe()
    print("\nmaking coffee with hook...")
    coffee_with_hook.prepare_recipe()

if __name__ == "__main__":
    main()