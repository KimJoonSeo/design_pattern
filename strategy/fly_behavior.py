from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print("저는 못 날아요. :(")


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print("슈슈슈웅~~")


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print("훨훨 날아갑니다~~")
