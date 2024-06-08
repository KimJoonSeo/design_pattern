from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def add_condiments(self):
        pass


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping coffe through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("adding lemon")