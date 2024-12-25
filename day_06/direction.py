from enum import Enum

from point import Point


class Direction(Enum):
    UP = Point(0, -1)
    RIGHT = Point(1, 0)
    DOWN = Point(0, 1)
    LEFT = Point(-1, 0)

    def move(self, position: 'Point') -> 'Point':
        return position + self.value
