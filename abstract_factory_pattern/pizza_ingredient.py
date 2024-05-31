from abc import ABC, abstractmethod


class Dough(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class ThickCrustDough(Dough):
    def __str__(self) -> str:
        return "ThickCrust style extra thick crust dough"


class ThinCrustDough(Dough):
    def __str__(self) -> str:
        return "Thin Crust Dough"


class Sauce(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class MarinaraSauce(Sauce):
    def __str__(self) -> str:
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def __str__(self) -> str:
        return "Tomato sauce with plum tomatoes"
