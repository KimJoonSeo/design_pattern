from abc import ABC, abstractmethod


class CaffeineBeverageWithHook(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
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

    def customer_wants_condiments(self):
        return True


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

    def customer_wants_condiments(self):
        ans: str = self._get_user_input()
        if ans.lower().startswith('y'):
            return True
        return False

    def _get_user_input(self):
        ans = input("Would you like lemon with your tea (y/n)?")
        return ans

class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print("Dripping Coffee through filter")

    def add_condiments(self):
        print("Adding Sugar and Milk")

    def customer_wants_condiments(self):
        ans: str = self._get_user_input()
        if ans.lower().startswith('y'):
            return True
        return False

    def _get_user_input(self):
        ans = input("Would you like milk and sugar with your coffee (y/n)?")
        return ans