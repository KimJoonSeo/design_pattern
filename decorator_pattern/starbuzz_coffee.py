from decorator_pattern.beverage import Beverage, Espresso, DarkRoast, HouseBlend
from decorator_pattern.condiment_decorator import Mocha, Whip, Soy


def main():
    beverage: Beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.cost()))

    beverage2: Beverage = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.cost()))

    beverage3: Beverage = \
        Whip(Mocha(Soy(HouseBlend())))
    print(beverage3.get_description() + " $" + str(beverage3.cost()))


if __name__ == "__main__":
    main()
