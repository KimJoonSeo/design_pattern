from abc import ABC, abstractmethod

from command_pattern.device import Light, GarageDoor


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class LightOnCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.on()


class GarageDoorOpenCommand(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.up()