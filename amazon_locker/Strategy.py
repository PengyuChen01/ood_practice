from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def assign_locker(self, package, lockers):
        pass

