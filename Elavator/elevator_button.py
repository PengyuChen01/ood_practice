from __future__ import annotations

from typing import TYPE_CHECKING

from .direction import Direction
from .request import ElevatorRequest

if TYPE_CHECKING:
    from .elevator import Elevator


class ElevatorButton:
    """Button panel inside an elevator for selecting a target floor."""

    def __init__(self, elevator: Elevator) -> None:
        self._elevator = elevator

    def press(self, target_floor: int) -> None:
        current = self._elevator.current_floor
        if target_floor == current:
            return
        direction = Direction.UP if target_floor > current else Direction.DOWN
        request = ElevatorRequest(
            target_floor=target_floor,
            direction=direction,
            is_external=False,
        )
        self._elevator.add_request(request)
        print(f"  [ElevatorButton] Elevator {self._elevator.elevator_id}: "
              f"floor {target_floor} selected")
