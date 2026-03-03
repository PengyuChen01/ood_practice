from .pizza import Pizza
from .pizza_decorator import PizzaDecorator


class SmallSize(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_price(self) -> float:
        return self._pizza.get_price() + 8.0

    def get_description(self) -> str:
        return f"Small {self._pizza.get_description()}"


class MediumSize(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_price(self) -> float:
        return self._pizza.get_price() + 10.0

    def get_description(self) -> str:
        return f"Medium {self._pizza.get_description()}"


class LargeSize(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_price(self) -> float:
        return self._pizza.get_price() + 12.0

    def get_description(self) -> str:
        return f"Large {self._pizza.get_description()}"
