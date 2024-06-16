
class GumballMachine:
    def __init__(self, number_gumballs) -> None:
        from state_pattern.state import NoQuarterState, SoldOutState, HasQuarterState, SoldState

        self.no_quarter_state = NoQuarterState(self)
        self.sold_out_state = SoldOutState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.count = number_gumballs
        if number_gumballs > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1

    def refill(self, count):
        self.count += count
        print(f"The gumball machine was just refilled; its new count is: {self.count}")
        self.state.refill()

    def set_state(self, state):
        self.state = state

    def __str__(self) -> str:
        result = ["\nMighty Gumball, Inc.", "\nJava-enabled Standing Gumball Model #2004",
                  f"\nInventory: {self.count} gumball"]
        if self.count != 1:
            result.append("s")

        result.append("\n")
        result.append(f"Machine is {self.state}\n")
        return "".join(result)