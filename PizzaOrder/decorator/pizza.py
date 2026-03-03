from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class BasePizza(Pizza):
    """Base pizza with no toppings, size, or type applied"""
    def get_price(self) -> float:
        return 0.0

    def get_description(self) -> str:
        return "Pizza"
