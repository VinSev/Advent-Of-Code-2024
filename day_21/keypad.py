from abc import ABC, abstractmethod
from functools import lru_cache
from typing import List, TYPE_CHECKING

from key_constants import START, EMPTY
from point import Point

if TYPE_CHECKING:
    from sequence_finder import SequenceFinder


class Keypad(ABC):
    def __init__(self, 
                 linked_keypad: 'Keypad', 
                 layout: List[List[str]], 
                 sequence_finder: 'SequenceFinder') -> None:
        self._linked_keypad = linked_keypad
        self._layout = layout
        self._sequence_finder = sequence_finder

        self.n_rows = len(self._layout)
        self.n_cols = len(self._layout[0])

    @abstractmethod
    def get_shortest_sequence_length(self, sequence: str) -> int:
        raise NotImplementedError

    def get_value_in_keypad_layout(self, position: Point) -> str:
        return self._layout[position.y][position.x]

    def get_position_in_keypad_layout(self, target: str) -> Point:
        for y, row in enumerate(self._layout):
            for x, value in enumerate(row):
                if value == target:
                    return Point(x, y)

        raise ValueError(f'{target} not found')
    
    def is_valid(self, position: Point) -> bool:
        return (self.is_out_of_bounds(position) or
                self.get_value_in_keypad_layout(position) == EMPTY)

    def is_out_of_bounds(self, position: Point) -> bool:
        return (position.x < 0 or position.y < 0 or
                position.x >= self.n_cols or position.y >= self.n_rows) 


class HumanControlledKeypad(Keypad):
    def get_shortest_sequence_length(self, sequence: str) -> int:
        return len(sequence)


class RobotControlledKeypad(Keypad):
    @lru_cache(maxsize=64)
    def get_shortest_sequence_length(self, sequence: str) -> int:
        total_length = self._get_shortest_sequence_length_between_keys(START, sequence[0])

        for i in range(len(sequence) - 1):
            current_key = sequence[i]
            next_key = sequence[i + 1]

            length = self._get_shortest_sequence_length_between_keys(current_key, next_key)
            total_length += length

        return total_length

    def _get_shortest_sequence_length_between_keys(self, start: str, end: str) -> int:
        sequences = self._sequence_finder.get_all_sequences(self, start, end)
        
        return min(self._linked_keypad.get_shortest_sequence_length(sequence) 
                   for sequence in sequences)

