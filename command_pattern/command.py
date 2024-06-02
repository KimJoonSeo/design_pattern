from abc import ABC, abstractmethod
from typing import List

from command_pattern.receiver import Light, GarageDoor, Stereo, CellingFan


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


class CellingFanHighCommand(Command):
    celling_fan: CellingFan
    prev_speed: int

    def __init__(self, celling_fan: CellingFan):
        self.celling_fan = celling_fan

    def execute(self) -> None:
        self.prev_speed = self.celling_fan.get_speed()
        self.celling_fan.high()

    def undo(self) -> None:
        if self.prev_speed == CellingFan.HIGH:
            self.celling_fan.high()
        elif self.prev_speed == CellingFan.MEDIUM:
            self.celling_fan.medium()
        elif self.prev_speed == CellingFan.LOW:
            self.celling_fan.low()
        elif self.prev_speed == CellingFan.OFF:
            self.celling_fan.off()


class CellingFanHighCommand(Command):
    celling_fan: CellingFan
    prev_speed: int

    def __init__(self, celling_fan: CellingFan):
        self.celling_fan = celling_fan

    def execute(self) -> None:
        self.prev_speed = self.celling_fan.get_speed()
        self.celling_fan.high()

    def undo(self) -> None:
        if self.prev_speed == CellingFan.HIGH:
            self.celling_fan.high()
        elif self.prev_speed == CellingFan.MEDIUM:
            self.celling_fan.medium()
        elif self.prev_speed == CellingFan.LOW:
            self.celling_fan.low()
        elif self.prev_speed == CellingFan.OFF:
            self.celling_fan.off()


class CellingFanOffCommand(Command):
    celling_fan: CellingFan
    prev_speed: int

    def __init__(self, celling_fan: CellingFan):
        self.celling_fan = celling_fan

    def execute(self) -> None:
        self.prev_speed = self.celling_fan.get_speed()
        self.celling_fan.off()

    def undo(self) -> None:
        if self.prev_speed == CellingFan.HIGH:
            self.celling_fan.high()
        elif self.prev_speed == CellingFan.MEDIUM:
            self.celling_fan.medium()
        elif self.prev_speed == CellingFan.LOW:
            self.celling_fan.low()
        elif self.prev_speed == CellingFan.OFF:
            self.celling_fan.off()


class CellingFanLowCommand(Command):
    celling_fan: CellingFan
    prev_speed: int

    def __init__(self, celling_fan: CellingFan):
        self.celling_fan = celling_fan

    def execute(self) -> None:
        self.prev_speed = self.celling_fan.get_speed()
        self.celling_fan.low()

    def undo(self) -> None:
        if self.prev_speed == CellingFan.HIGH:
            self.celling_fan.high()
        elif self.prev_speed == CellingFan.MEDIUM:
            self.celling_fan.medium()
        elif self.prev_speed == CellingFan.LOW:
            self.celling_fan.low()
        elif self.prev_speed == CellingFan.OFF:
            self.celling_fan.off()


class CellingFanMediumCommand(Command):
    celling_fan: CellingFan
    prev_speed: int

    def __init__(self, celling_fan: CellingFan):
        self.celling_fan = celling_fan

    def execute(self) -> None:
        self.prev_speed = self.celling_fan.get_speed()
        self.celling_fan.medium()

    def undo(self) -> None:
        if self.prev_speed == CellingFan.HIGH:
            self.celling_fan.high()
        elif self.prev_speed == CellingFan.MEDIUM:
            self.celling_fan.medium()
        elif self.prev_speed == CellingFan.LOW:
            self.celling_fan.low()
        elif self.prev_speed == CellingFan.OFF:
            self.celling_fan.off()


class MacroCommand(Command):
    commands: List[Command]

    def __init__(self, commands):
        self.commands = commands

    def undo(self) -> None:
        for command in self.commands:
            command.undo()

    def execute(self) -> None:
        for command in self.commands:
            command.execute()
