from abc import ABC


class Pizza(ABC):
    name: str
    dough: str
    sauce: str

    def prepare(self) -> None:
        print("Prepare")

    def bake(self) -> None:
        print("Bake")

    def cut(self) -> None:
        print("Cut")

    def box(self) -> None:
        print("Box")

    def get_name(self) -> str:
        return self.name


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "시카고 스타일 치즈 피자"
        self.dough = "두꺼운 크러스트 도우"
        self.sauce = "플럼토마토 소스"

    def prepare(self) -> None:
        super().prepare()
        print("Add cheese")

    def bake(self) -> None:
        super().bake()

    def cut(self) -> None:
        super().cut()

    def box(self) -> None:
        super().box()


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name = "시카고 스타일 야채 피자"
        self.dough = "두꺼운 크러스트 도우"
        self.sauce = "플럼토마토 소스"

    def prepare(self) -> None:
        super().prepare()
        print("Add vegitable")

    def bake(self) -> None:
        super().bake()

    def cut(self) -> None:
        super().cut()

    def box(self) -> None:
        super().box()


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "뉴욕 스타일 소스와 치즈 피자"
        self.dough = "씬 크러스트 도우"
        self.sauce = "마리나라 소스"

    def prepare(self) -> None:
        super().prepare()
        print("Add cheese")

    def bake(self) -> None:
        super().bake()

    def cut(self) -> None:
        super().cut()

    def box(self) -> None:
        super().box()


class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name = "뉴욕 스타일 소스와 페페로니 피자"
        self.dough = "씬 크러스트 도우"
        self.sauce = "마리나라 소스"

    def prepare(self) -> None:
        super().prepare()
        print("Add pepperoni")

    def bake(self) -> None:
        super().bake()

    def cut(self) -> None:
        super().cut()

    def box(self) -> None:
        super().box()
