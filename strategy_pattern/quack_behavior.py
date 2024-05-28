from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self) -> None:
        pass


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print('조용~~')


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print('삑삑~~')


class Quack(QuackBehavior):
    def quack(self) -> None:
        print('꽥~~꽥~~')
