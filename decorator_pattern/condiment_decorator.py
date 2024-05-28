from abc import abstractmethod

from decorator_pattern.beverage import Beverage


class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Mocha(CondimentDecorator):
    _beverage: Beverage

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ", 모카"

    def cost(self) -> float:
        return self._beverage.cost() + 0.2


class Soy(CondimentDecorator):
    _beverage: Beverage

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ", 두유"

    def cost(self) -> float:
        return self._beverage.cost() + 0.15


class Whip(CondimentDecorator):
    _beverage: Beverage

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description() + ", 휘핑 크림"

    def cost(self) -> float:
        return self._beverage.cost() + 0.1
