from .pizza import Pizza
from .pizza_decorator import PizzaDecorator


class BananaTopping(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_price(self) -> float:
        return self._pizza.get_price() + 1.5

    def get_description(self) -> str:
        return f"{self._pizza.get_description()} + Banana"


class MushroomTopping(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_price(self) -> float:
        return self._pizza.get_price() + 2.0

    def get_description(self) -> str:
        return f"{self._pizza.get_description()} + Mushroom"


class CheeseTopping(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_price(self) -> float:
        return self._pizza.get_price() + 2.5

    def get_description(self) -> str:
        return f"{self._pizza.get_description()} + Cheese"
