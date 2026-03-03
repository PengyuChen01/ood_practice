from abc import ABC, abstractmethod


class SizeStrategy(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass


class SmallSize(SizeStrategy):
    def get_price(self) -> float:
        return 8.0


class MediumSize(SizeStrategy):
    def get_price(self) -> float:
        return 10.0


class LargeSize(SizeStrategy):
    def get_price(self) -> float:
        return 12.0
