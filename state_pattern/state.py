from state_pattern.gumball_machine import GumballMachine


class State:
    def insert_quarter(self):
        raise NotImplementedError

    def eject_quarter(self):
        raise NotImplementedError

    def turn_crank(self):
        raise NotImplementedError

    def dispense(self):
        raise NotImplementedError

    def refill(self):
        raise NotImplementedError


class NoQuarterState(State):
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You inserted a quarter")
        self.gumball_machine.set_state(self.gumball_machine.has_quarter_state)

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")

    def refill(self):
        raise NotImplementedError

    def __str__(self):
        return "waiting for quarter"


class SoldOutState(State):
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turn_crank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)

    def __str__(self):
        return "sold out"


class HasQuarterState(State):
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)

    def turn_crank(self):
        print("You turned...")
        self.gumball_machine.set_state(self.gumball_machine.sold_state)

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        raise NotImplementedError

    def __str__(self):
        return "waiting for turn of crank"


class SoldState(State):
    def __init__(self, gumball_machine: GumballMachine) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.count > 0:
            self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)
        else:
            self.gumball_machine.set_state(self.gumball_machine.sold_out_state)

    def refill(self):
        raise NotImplementedError

    def __str__(self):
        return "dispensing a gumball"