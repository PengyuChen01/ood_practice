from dataclasses import dataclass

from .direction import Direction


@dataclass
class ElevatorRequest:
    target_floor: int
    direction: Direction
    is_external: bool = False
