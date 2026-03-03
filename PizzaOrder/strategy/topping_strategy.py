from abc import ABC, abstractmethod


class ToppingStrategy(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass


class BananaTopping(ToppingStrategy):
    def get_price(self) -> float:
        return 1.5


class MushroomTopping(ToppingStrategy):
    def get_price(self) -> float:
        return 2.0


class CheeseTopping(ToppingStrategy):
    def get_price(self) -> float:
        return 2.5


class NoTopping(ToppingStrategy):
    def get_price(self) -> float:
        return 0.0
