from abc import ABC
from .pizza import Pizza


class PizzaDecorator(Pizza, ABC):
    """Base decorator that wraps a Pizza"""
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def get_price(self) -> float:
        return self._pizza.get_price()

    def get_description(self) -> str:
        return self._pizza.get_description()
