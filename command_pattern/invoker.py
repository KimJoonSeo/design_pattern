from typing import List, Optional, Any

from command_pattern.command import Command


class SimpleRemoteControl:
    slot: Command

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


class RemoteControl:
    on_commands: List[Optional[Command]]
    off_commands: List[Optional[Command]]
    undo_command: Optional[Command]

    def __init__(self) -> None:
        self.on_commands = [None] * 7
        self.off_commands = [None] * 7
        self.undo_command = None

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        if self.on_commands[slot]:
            self.on_commands[slot].execute()
            self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot: int):
        if self.off_commands[slot]:
            self.off_commands[slot].execute()
            self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        if self.undo_command:
            self.undo_command.undo()

    def __str__(self):
        res: str = "\n------리모컨------\n"
        for i in range(len(self.on_commands)):
            if self.on_commands[i] and self.off_commands[i]:
                res += '[slot {}] {} {} \n'.format(str(i),
                                                   type(self.on_commands[i]).__name__,
                                                   type(self.off_commands[i]).__name__)
            else:
                res += '[slot {}] {} {} \n'.format(str(i),
                                                   "NoCommand",
                                                   "NoCommand")

        res += '[Undo] {}'.format(type(self.undo_command).__name__ if self.undo_command else 'None')

        return res
