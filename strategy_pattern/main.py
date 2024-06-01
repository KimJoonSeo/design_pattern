from strategy_pattern.duck import Duck, DecoyDuck, MallardDuck, RubberDuck
from strategy_pattern.fly_behavior import FlyRocketPowered


def main():
    # Upcasting
    mallard: Duck = MallardDuck()
    rubber: Duck = RubberDuck()
    decoy: Duck = DecoyDuck()

    mallard.perform_quack()
    mallard.perform_fly()
    mallard.swim()
    mallard.display()

    rubber.perform_quack()
    rubber.perform_fly()
    rubber.swim()
    rubber.display()

    decoy.perform_quack()
    decoy.perform_fly()
    decoy.swim()
    decoy.display()
    decoy.set_fly_behavior(FlyRocketPowered())
    decoy.perform_fly()


if __name__ == "__main__":
    main() 