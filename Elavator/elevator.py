from sortedcontainers import SortedList

from .direction import Direction
from .request import ElevatorRequest


class Elevator:
    """Single elevator using the SCAN (elevator) algorithm."""

    def __init__(self, elevator_id: int, max_floor: int) -> None:
        self._elevator_id = elevator_id
        self._max_floor = max_floor
        self._current_floor: int = 1
        self._direction: Direction = Direction.IDLE
        # Ascending order for up requests, descending for down requests
        self._up_requests: SortedList[int] = SortedList()
        self._down_requests: SortedList[int] = SortedList()

    # -- public properties --

    @property
    def elevator_id(self) -> int:
        return self._elevator_id

    @property
    def current_floor(self) -> int:
        return self._current_floor

    @property
    def direction(self) -> Direction:
        return self._direction

    @property
    def is_idle(self) -> bool:
        return (self._direction == Direction.IDLE
                and len(self._up_requests) == 0
                and len(self._down_requests) == 0)

    # -- request handling --

    def add_request(self, request: ElevatorRequest) -> None:
        floor = request.target_floor
        if floor == self._current_floor:
            print(f"    Elevator {self._elevator_id}: already at floor {floor}")
            return

        if floor > self._current_floor:
            if floor not in self._up_requests:
                self._up_requests.add(floor)
        else:
            if floor not in self._down_requests:
                self._down_requests.add(floor)

        # Wake up if idle
        if self._direction == Direction.IDLE:
            if floor > self._current_floor:
                self._direction = Direction.UP
            else:
                self._direction = Direction.DOWN

    # -- simulation --

    def step(self) -> None:
        """Move one floor in the current direction and handle arrivals."""
        if self._direction == Direction.IDLE:
            return

        self._current_floor += self._direction.value
        print(f"    Elevator {self._elevator_id}: -> floor {self._current_floor}")

        # Check if we've arrived at a requested floor
        if (self._direction == Direction.UP
                and self._current_floor in self._up_requests):
            self._up_requests.remove(self._current_floor)
            print(f"    Elevator {self._elevator_id}: *STOP* at floor "
                  f"{self._current_floor}")

        elif (self._direction == Direction.DOWN
              and self._current_floor in self._down_requests):
            self._down_requests.remove(self._current_floor)
            print(f"    Elevator {self._elevator_id}: *STOP* at floor "
                  f"{self._current_floor}")

        # Decide next direction
        self._update_direction()

    def _update_direction(self) -> None:
        if self._direction == Direction.UP:
            if self._up_requests:
                return  # keep going up
            if self._down_requests:
                self._direction = Direction.DOWN
            else:
                self._direction = Direction.IDLE
        elif self._direction == Direction.DOWN:
            if self._down_requests:
                return  # keep going down
            if self._up_requests:
                self._direction = Direction.UP
            else:
                self._direction = Direction.IDLE

    def process_requests(self) -> None:
        """Run step() until all requests are served."""
        print(f"  Elevator {self._elevator_id} starts at floor "
              f"{self._current_floor}, direction={self._direction.name}")
        while not self.is_idle:
            self.step()
        print(f"  Elevator {self._elevator_id} is now IDLE at floor "
              f"{self._current_floor}")

    def __repr__(self) -> str:
        return (f"Elevator({self._elevator_id}, floor={self._current_floor}, "
                f"dir={self._direction.name})")
