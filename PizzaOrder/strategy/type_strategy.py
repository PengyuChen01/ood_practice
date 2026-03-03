from abc import ABC, abstractmethod


class TypeStrategy(ABC):
    @abstractmethod
    def get_multiplier(self) -> float:
        pass


class TexasType(TypeStrategy):
    def get_multiplier(self) -> float:
        return 1.2


class CaliforniaType(TypeStrategy):
    def get_multiplier(self) -> float:
        return 1.1


class NewYorkType(TypeStrategy):
    def get_multiplier(self) -> float:
        return 1.0
