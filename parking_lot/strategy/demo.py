"""Strategy Pattern Demo - Parking Lot"""
from .vehicle import Vehicle, VehicleType
from .parking_spot import ParkingSpot, SpotSize
from .pricing_strategy import HourlyPricing, FlatPricing, MemberPricing
from .parking_lot import ParkingLot


def main():
    # === Hourly pricing parking lot ===
    hourly_lot = ParkingLot("Downtown Garage", pricing=HourlyPricing())
    hourly_lot.add_spot(ParkingSpot("A1", SpotSize.SMALL))
    hourly_lot.add_spot(ParkingSpot("A2", SpotSize.MEDIUM))
    hourly_lot.add_spot(ParkingSpot("A3", SpotSize.MEDIUM))
    hourly_lot.add_spot(ParkingSpot("A4", SpotSize.LARGE))

    car = Vehicle("ABC-123", VehicleType.CAR)
    ticket = hourly_lot.park(car)
    print(f"Parked {car.license_plate}, ticket: {ticket.ticket_id}")
    print(f"Available: {hourly_lot.available_spots()}")

    # checkout (minimum 1 hour)
    price = hourly_lot.leave("ABC-123")
    print(f"Hourly price for car: ${price:.2f}")

    # === Same car, flat pricing lot ===
    flat_lot = ParkingLot("Airport Lot", pricing=FlatPricing())
    flat_lot.add_spot(ParkingSpot("B1", SpotSize.MEDIUM))

    ticket2 = flat_lot.park(car)
    price2 = flat_lot.leave("ABC-123")
    print(f"Flat price for car: ${price2:.2f}")

    # === Member pricing ===
    member_lot = ParkingLot("Office Garage", pricing=MemberPricing())
    member_lot.add_spot(ParkingSpot("C1", SpotSize.MEDIUM))

    ticket3 = member_lot.park(car)
    price3 = member_lot.leave("ABC-123")
    print(f"Member price for car: ${price3:.2f}")


if __name__ == "__main__":
    main()
