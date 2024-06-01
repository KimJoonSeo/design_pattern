from command_pattern.command import LightOnCommand, GarageDoorOpenCommand
from command_pattern.device import Light, GarageDoor
from command_pattern.remote_control import SimpleRemoteControl


def main():
    remote = SimpleRemoteControl()
    light = Light()
    light_on: LightOnCommand = LightOnCommand(light)
    garage_door = GarageDoor()
    garage_door_open = GarageDoorOpenCommand(garage_door)

    remote.set_command(light_on)
    remote.button_was_pressed()
    remote.set_command(garage_door_open)
    remote.button_was_pressed()


if __name__ == "__main__":
    main()