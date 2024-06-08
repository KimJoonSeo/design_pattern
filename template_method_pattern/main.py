from template_method_pattern.caffeine_beverage import Tea, Coffee


def main():
    tea = Tea()
    coffee = Coffee()

    print("\nmaking tea...")
    tea.prepare_recipe()
    print("\nmaking coffee...")
    coffee.prepare_recipe()

if __name__ == "__main__":
    main()