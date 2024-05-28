from abc import ABC, abstractmethod

from strategy_pattern.fly_behavior import FlyBehavior, FlyNoWay, FlyWithWings
from strategy_pattern.quack_behavior import QuackBehavior, MuteQuack, Quack, Squeak


class Duck(ABC):
    quack_behavior: QuackBehavior
    fly_behavior: FlyBehavior

    def swim(self) -> None:
        print('둥둥~~')

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def set_quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self.quack_behavior = quack_behavior

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self.fly_behavior = fly_behavior

    @abstractmethod
    def display(self) -> None:
        pass


class DecoyDuck(Duck):
    def __init__(self):
        self.quack_behavior = MuteQuack()
        self.fly_behavior = FlyNoWay()

    def display(self) -> None:
        print("나는 나무 오리~")


class MallardDuck(Duck):
    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def display(self) -> None:
        print("나는 청둥오리~")


class RubberDuck(Duck):
    def __init__(self):
        self.quack_behavior = Squeak()
        self.fly_behavior = FlyNoWay()

    def display(self) -> None:
        print("나는 고무 오리~")

