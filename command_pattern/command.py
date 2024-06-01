from abc import ABC, abstractmethod

from command_pattern.receiver import Light, GarageDoor, Stereo


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightOnCommand(Command):
    def undo(self) -> None:
        self.light.off()

    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.on()


class LightOffCommand(Command):
    def undo(self) -> None:
        self.light.on()

    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.off()


class GarageDoorOpenCommand(Command):
    def undo(self) -> None:
        self.garage_door.off()

    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.up()


class GarageDoorCloseCommand(Command):
    def undo(self) -> None:
        self.garage_door.up()

    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.off()


class StereoOnWithCDCommand(Command):
    def undo(self) -> None:
        self.stereo.off()

    stereo: Stereo

    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)


class StereoOffCommand(Command):
    def undo(self) -> None:
        self.stereo.on()

    stereo: Stereo

    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.off()
