from .pizza import Pizza
from .pizza_decorator import PizzaDecorator


class TexasType(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_price(self) -> float:
        return self._pizza.get_price() * 1.2

    def get_description(self) -> str:
        return f"{self._pizza.get_description()} (Texas Style)"


class CaliforniaType(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_price(self) -> float:
        return self._pizza.get_price() * 1.1

    def get_description(self) -> str:
        return f"{self._pizza.get_description()} (California Style)"


class NewYorkType(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_price(self) -> float:
        return self._pizza.get_price() * 1.0

    def get_description(self) -> str:
        return f"{self._pizza.get_description()} (New York Style)"
