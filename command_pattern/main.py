from command_pattern.command import LightOnCommand, GarageDoorOpenCommand, LightOffCommand, GarageDoorCloseCommand, \
    StereoOffCommand, StereoOnWithCDCommand, CellingFanMediumCommand, CellingFanHighCommand, CellingFanOffCommand, \
    CellingFanLowCommand
from command_pattern.receiver import Light, GarageDoor, Stereo, CellingFan
from command_pattern.invoker import SimpleRemoteControl, RemoteControl


def main():
    # remote = SimpleRemoteControl()
    # light = Light()
    # light_on: LightOnCommand = LightOnCommand(light)
    # garage_door = GarageDoor()
    # garage_door_open = GarageDoorOpenCommand(garage_door)
    #
    # remote.set_command(light_on)
    # remote.button_was_pressed()
    # remote.set_command(garage_door_open)
    # remote.button_was_pressed()

    remote_control = RemoteControl()

    living_room_lignt = Light()
    kitchen_light = Light()
    garage_door = GarageDoor()
    stereo = Stereo()

    living_room_light_on = LightOnCommand(living_room_lignt)
    living_room_light_off = LightOffCommand(living_room_lignt)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)
    garage_door_open = GarageDoorOpenCommand(garage_door)
    garage_door_close = GarageDoorCloseCommand(garage_door)
    stereo_on = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, garage_door_open, garage_door_close)
    remote_control.set_command(3, stereo_on, stereo_off)


    print(str(remote_control))

    remote_control.on_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.on_button_was_pushed(3)

    remote_control.off_button_was_pushed(0)
    remote_control.off_button_was_pushed(1)
    remote_control.off_button_was_pushed(2)
    remote_control.off_button_was_pushed(3)
    print('before push undo')
    remote_control.undo_button_was_pushed()
    print('after push undo')
    print(str(remote_control))


    print("------------선풍기 Command TEST--------------")
    remote_control_undo = RemoteControl()
    celling_fan = CellingFan("living room")

    fan_medium_command = CellingFanMediumCommand(celling_fan)
    fan_high_command = CellingFanHighCommand(celling_fan)
    fan_off_command = CellingFanOffCommand(celling_fan)
    fan_low_command = CellingFanLowCommand(celling_fan)

    remote_control_undo.set_command(0, fan_medium_command, fan_off_command)
    remote_control_undo.set_command(1, fan_high_command, fan_off_command)
    remote_control_undo.on_button_was_pushed(0)
    remote_control_undo.off_button_was_pushed(0)
    print(str(remote_control_undo))
    remote_control_undo.undo_button_was_pushed()

    remote_control_undo.on_button_was_pushed(1)
    print(str(remote_control_undo))
    remote_control_undo.undo_button_was_pushed()
    print(str(remote_control_undo))




if __name__ == "__main__":
    main()
