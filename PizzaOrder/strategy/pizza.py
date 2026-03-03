from typing import List
from .size_strategy import SizeStrategy
from .topping_strategy import ToppingStrategy
from .type_strategy import TypeStrategy


class Pizza:
    def __init__(
        self,
        size: SizeStrategy,
        pizza_type: TypeStrategy,
        toppings: List[ToppingStrategy] = None
    ):
        self._size = size
        self._type = pizza_type
        self._toppings = toppings or []

    def add_topping(self, topping: ToppingStrategy):
        self._toppings.append(topping)

    def get_price(self) -> float:
        base_price = self._size.get_price()
        topping_price = sum(t.get_price() for t in self._toppings)
        subtotal = base_price + topping_price
        return subtotal * self._type.get_multiplier()
