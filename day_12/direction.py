from enum import Enum
from typing import Tuple


class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def move(self, x: int, y: int) -> Tuple[int, int]:
        return x + self.value[0], y + self.value[1]

DIRECTIONS = list(Direction)