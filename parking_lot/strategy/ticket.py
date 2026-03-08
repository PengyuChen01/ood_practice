from datetime import datetime
from .vehicle import Vehicle
from .parking_spot import ParkingSpot
from .pricing_strategy import PricingStrategy


class Ticket:
    def __init__(
        self,
        ticket_id: str,
        vehicle: Vehicle,
        spot: ParkingSpot,
        pricing: PricingStrategy
    ):
        self._ticket_id = ticket_id
        self._vehicle = vehicle
        self._spot = spot
        self._pricing = pricing
        self._entry_time = datetime.now()
        self._exit_time: datetime = None

    @property
    def ticket_id(self) -> str:
        return self._ticket_id

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle

    @property
    def spot(self) -> ParkingSpot:
        return self._spot

    def checkout(self) -> float:
        self._exit_time = datetime.now()
        hours = (self._exit_time - self._entry_time).total_seconds() / 3600
        hours = max(hours, 1.0)  # minimum 1 hour charge
        return self._pricing.calculate_price(hours, self._spot.size)
