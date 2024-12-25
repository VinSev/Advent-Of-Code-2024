from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

from key_constants import UP, RIGHT, DOWN, LEFT, START, EMPTY
from point import Point

if TYPE_CHECKING:
    from keypad import Keypad


AXES = {
    'x': {
        0: (LEFT, Point(-1, 0)), 
        1: (RIGHT, Point(1, 0))
    },
    'y': {
        0: (UP, Point(0, -1)), 
        1: (DOWN, Point(0, 1))
    }
}


class SequenceFinder(ABC):
    @abstractmethod
    def get_all_sequences(self, 
                          keypad: 'Keypad', 
                          start: str, 
                          end: str) -> List[str]:
        raise NotImplementedError


class DFS(SequenceFinder):
    def __init__(self) -> None:
        self._keypad = None
        self._sequences = []
        self._current_sequence = ''

    def get_all_sequences(self, 
                          keypad: 'Keypad', 
                          start: str, 
                          end: str) -> List[str]:
        self._keypad = keypad
        self._sequences = []

        start_position = keypad.get_position_in_keypad_layout(start)
        end_position = keypad.get_position_in_keypad_layout(end)

        movement_vector = start_position - end_position

        self._dfs(movement_vector, end_position)

        return self._sequences

    def _dfs(self, movement_vector: Point, target: Point) -> None:
        new_position = movement_vector + target

        if self._keypad.is_valid(new_position):
            return

        if movement_vector.x == 0 and movement_vector.y == 0:
            self._sequences.append(self._current_sequence + START)
            return

        self._move(movement_vector, target)

    def _move(self, movement_vector: Point, target: Point) -> None:
        self._move_in_direction('y', movement_vector, target)
        self._move_in_direction('x', movement_vector, target)

    def _move_in_direction(self, 
                           axis: str, 
                           movement_vector: Point, 
                           target: Point) -> None:
        axis_movement_value = getattr(movement_vector, axis)

        if axis_movement_value != 0:
            direction_index = 0 if axis_movement_value > 0 else 1
            direction_symbol, direction = AXES[axis][direction_index]

            self._current_sequence += direction_symbol
            self._dfs(movement_vector + direction, target)
            self._current_sequence = self._current_sequence[:-1]
