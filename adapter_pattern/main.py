from adapter_pattern.adapter import TurkeyAdapter
from adapter_pattern.duck import MallardDuck, Duck
from adapter_pattern.turkey import Turkey, WildTurkey


def test_duck(duck: Duck):
    duck.quack()
    duck.fly()


def main():
    duck: Duck = MallardDuck()
    turkey: Turkey = WildTurkey()
    turkey_adapter: Duck = TurkeyAdapter(turkey)

    print("\nThe Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    test_duck(duck)

    print("\nThe Duck Adapter says...")
    test_duck(turkey_adapter)


if __name__ == "__main__":
    main()
