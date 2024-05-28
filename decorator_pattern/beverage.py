from abc import ABC, abstractmethod


class Beverage(ABC):
    _description: str = "설명 없음"

    def get_description(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        pass


class Espresso(Beverage):
    def __init__(self):
        self._description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        self._description = '하우스 블렌드'

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def __init__(self):
        self._description = '다크로스트'

    def cost(self) -> float:
        return 0.99


