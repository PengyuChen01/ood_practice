from abc import ABC, abstractmethod
from .parking_spot import SpotSize


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, hours: float, spot_size: SpotSize) -> float:
        pass


class HourlyPricing(PricingStrategy):
    """charge per hour, rate depends on spot size"""

    RATES = {
        SpotSize.SMALL: 2.0,
        SpotSize.MEDIUM: 5.0,
        SpotSize.LARGE: 8.0,
    }

    def calculate_price(self, hours: float, spot_size: SpotSize) -> float:
        rate = self.RATES[spot_size]
        return rate * hours


class FlatPricing(PricingStrategy):
    """flat rate per entry, regardless of time"""

    RATES = {
        SpotSize.SMALL: 10.0,
        SpotSize.MEDIUM: 20.0,
        SpotSize.LARGE: 30.0,
    }

    def calculate_price(self, hours: float, spot_size: SpotSize) -> float:
        return self.RATES[spot_size]


class MemberPricing(PricingStrategy):
    """member discount: 50% off hourly rate"""

    RATES = {
        SpotSize.SMALL: 1.0,
        SpotSize.MEDIUM: 2.5,
        SpotSize.LARGE: 4.0,
    }

    def calculate_price(self, hours: float, spot_size: SpotSize) -> float:
        rate = self.RATES[spot_size]
        return rate * hours
