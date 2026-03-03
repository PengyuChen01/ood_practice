from __future__ import annotations

from typing import TYPE_CHECKING

from .direction import Direction
from .request import ElevatorRequest

if TYPE_CHECKING:
    from .elevator_system import ElevatorSystem


class FloorButton:
    """Up/Down buttons on a floor that dispatch requests to the system."""

    def __init__(self, floor: int, system: ElevatorSystem) -> None:
        self._floor = floor
        self._system = system

    def press_up(self) -> None:
        request = ElevatorRequest(
            target_floor=self._floor,
            direction=Direction.UP,
            is_external=True,
        )
        print(f"  [FloorButton] Floor {self._floor}: UP pressed")
        self._system.dispatch(request)

    def press_down(self) -> None:
        request = ElevatorRequest(
            target_floor=self._floor,
            direction=Direction.DOWN,
            is_external=True,
        )
        print(f"  [FloorButton] Floor {self._floor}: DOWN pressed")
        self._system.dispatch(request)
