from abc import ABC, abstractmethod


class Turkey(ABC):
    @abstractmethod
    def gobble(self) -> None:
        pass

    @abstractmethod
    def fly(self) -> None:
        pass

class WildTurkey(Turkey):
    def gobble(self) -> None:
        print("Gobble gobble")

    def fly(self) -> None:
        print("I'm flying a short distance")