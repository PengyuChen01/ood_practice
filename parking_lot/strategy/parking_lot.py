from typing import Dict, List, Optional
from .vehicle import Vehicle
from .parking_spot import ParkingSpot, SpotSize
from .pricing_strategy import PricingStrategy
from .ticket import Ticket


class ParkingLot:
    def __init__(self, name: str, pricing: PricingStrategy):
        self._name = name
        self._pricing = pricing
        self._spots: List[ParkingSpot] = []
        self._active_tickets: Dict[str, Ticket] = {}  # license_plate -> ticket
        self._ticket_counter = 0

    def add_spot(self, spot: ParkingSpot):
        self._spots.append(spot)

    def _find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        for spot in self._spots:
            if spot.is_available() and spot.can_fit(vehicle):
                return spot
        return None

    def park(self, vehicle: Vehicle) -> Ticket:
        if vehicle.license_plate in self._active_tickets:
            raise Exception(f"Vehicle {vehicle.license_plate} is already parked")

        spot = self._find_available_spot(vehicle)
        if spot is None:
            raise Exception("No available spot for this vehicle")

        spot.park(vehicle)
        self._ticket_counter += 1
        ticket = Ticket(
            ticket_id=f"T-{self._ticket_counter:04d}",
            vehicle=vehicle,
            spot=spot,
            pricing=self._pricing
        )
        self._active_tickets[vehicle.license_plate] = ticket
        return ticket

    def leave(self, license_plate: str) -> float:
        if license_plate not in self._active_tickets:
            raise Exception(f"No active ticket for {license_plate}")

        ticket = self._active_tickets.pop(license_plate)
        price = ticket.checkout()
        ticket.spot.remove_vehicle()
        return price

    def available_spots(self) -> Dict[SpotSize, int]:
        counts = {size: 0 for size in SpotSize}
        for spot in self._spots:
            if spot.is_available():
                counts[spot.size] += 1
        return counts
