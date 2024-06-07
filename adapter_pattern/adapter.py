import random

from adapter_pattern.duck import Duck
from adapter_pattern.turkey import Turkey


class TurkeyAdapter(Duck):
    turkey: Turkey

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        for _ in range(5):
            self.turkey.fly()


class DuckAdapter(Turkey):
    duck: Duck
    def __init__(self, duck: Duck):
        self.duck = duck
    def gobble(self) -> None:
        self.duck.quack()

    def fly(self) -> None:
        num = random.choice([1,2,3,4,5])
        if num == 5:
            self.duck.fly()