from .direction import Direction
from .elevator import Elevator
from .floor_button import FloorButton
from .request import ElevatorRequest


class ElevatorSystem:
    """Multi-elevator dispatcher using a scoring algorithm."""

    def __init__(self, num_elevators: int, max_floor: int) -> None:
        self._max_floor = max_floor
        self._elevators = [
            Elevator(i, max_floor) for i in range(num_elevators)
        ]
        # Floor buttons: floors 1..max_floor
        self._floor_buttons = {
            f: FloorButton(f, self) for f in range(1, max_floor + 1)
        }

    # -- public accessors --

    @property
    def elevators(self) -> list[Elevator]:
        return list(self._elevators)

    def floor_button(self, floor: int) -> FloorButton:
        return self._floor_buttons[floor]

    def elevator_button_press(self, elevator_id: int, target_floor: int) -> None:
        """Simulate pressing a floor button inside a specific elevator."""
        elevator = self._elevators[elevator_id]
        current = elevator.current_floor
        if target_floor == current:
            return
        direction = Direction.UP if target_floor > current else Direction.DOWN
        request = ElevatorRequest(
            target_floor=target_floor,
            direction=direction,
            is_external=False,
        )
        elevator.add_request(request)
        print(f"  [InternalButton] Elevator {elevator_id}: "
              f"floor {target_floor} selected")

    # -- dispatching --

    def dispatch(self, request: ElevatorRequest) -> None:
        best = self._select_elevator(request)
        print(f"  => Dispatched to Elevator {best.elevator_id}")
        best.add_request(request)

    def _select_elevator(self, request: ElevatorRequest) -> Elevator:
        best_elevator = self._elevators[0]
        best_score = float("inf")

        for elevator in self._elevators:
            score = self._score(elevator, request)
            if score < best_score:
                best_score = score
                best_elevator = elevator

        return best_elevator

    def _score(self, elevator: Elevator, request: ElevatorRequest) -> float:
        distance = abs(elevator.current_floor - request.target_floor)

        # Case 1: elevator is idle
        if elevator.is_idle:
            return distance + self._max_floor

        same_direction = (elevator.direction == request.direction)

        if same_direction:
            on_the_way = (
                (request.direction == Direction.UP
                 and request.target_floor >= elevator.current_floor)
                or
                (request.direction == Direction.DOWN
                 and request.target_floor <= elevator.current_floor)
            )
            if on_the_way:
                # Case 2: same direction and on the way – best non-idle score
                return distance
            # Case 3: same direction but already passed
            return distance + 2 * self._max_floor

        # Case 4: opposite direction
        return distance + 3 * self._max_floor

    # -- simulation --

    def process_all(self) -> None:
        """Process all pending requests across all elevators."""
        for elevator in self._elevators:
            if not elevator.is_idle:
                elevator.process_requests()

    def status(self) -> None:
        print("  --- System Status ---")
        for e in self._elevators:
            print(f"    {e}")
        print()
