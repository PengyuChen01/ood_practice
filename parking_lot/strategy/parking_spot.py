from enum import Enum
from .vehicle import Vehicle, VehicleType


class SpotSize(Enum):
    SMALL = "small"        # for motorcycle
    MEDIUM = "medium"      # for car
    LARGE = "large"        # for truck


# which spot size can fit which vehicle types
SPOT_COMPATIBILITY = {
    SpotSize.SMALL: {VehicleType.MOTORCYCLE},
    SpotSize.MEDIUM: {VehicleType.MOTORCYCLE, VehicleType.CAR},
    SpotSize.LARGE: {VehicleType.MOTORCYCLE, VehicleType.CAR, VehicleType.TRUCK},
}


class ParkingSpot:
    def __init__(self, spot_id: str, size: SpotSize):
        self._spot_id = spot_id
        self._size = size
        self._vehicle: Vehicle = None

    @property
    def spot_id(self) -> str:
        return self._spot_id

    @property
    def size(self) -> SpotSize:
        return self._size

    def is_available(self) -> bool:
        return self._vehicle is None

    def can_fit(self, vehicle: Vehicle) -> bool:
        return vehicle.vehicle_type in SPOT_COMPATIBILITY[self._size]

    def park(self, vehicle: Vehicle):
        if not self.is_available():
            raise Exception(f"Spot {self._spot_id} is occupied")
        if not self.can_fit(vehicle):
            raise Exception(f"Vehicle {vehicle.license_plate} cannot fit in spot {self._spot_id}")
        self._vehicle = vehicle

    def remove_vehicle(self) -> Vehicle:
        if self.is_available():
            raise Exception(f"Spot {self._spot_id} is already empty")
        vehicle = self._vehicle
        self._vehicle = None
        return vehicle
