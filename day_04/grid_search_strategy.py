from abc import ABC, abstractmethod
from typing import List

from grid import Grid


class GridSearchStrategy(ABC):
    @abstractmethod
    def search(self) -> int:
        raise NotImplementedError


class WordSearchStrategy(GridSearchStrategy):
    def __init__(self, grid: 'Grid', direction_deltas: List[int], target_word: str) -> None:
        self._grid = grid
        self._direction_deltas = direction_deltas
        self._target_word = target_word
        
        self._rows, self._cols = self._grid.get_size()
        
    def search(self) -> int:
        occurrences = 0
        
        for row in range(self._rows):
            for col in range(self._cols):
                occurrences += self._is_word_in_directions_from_position(row, col)
                
        return occurrences

    def _is_word_in_directions_from_position(self, row: int, col: int) -> int:
        occurrences = 0
        
        for row_delta in self._direction_deltas:
            for col_delta in self._direction_deltas:
                if self._is_word_in_direction(row, col, row_delta, col_delta):
                    occurrences += 1
                    
        return occurrences

    def _is_word_in_direction(self, row: int, col: int, row_delta: int, col_delta: int) -> bool:
        for i in range(len(self._target_word)):
            current_row = row + row_delta * i
            current_col = col + col_delta * i

            if not self._grid.is_valid_position(current_row, current_col) or self._grid.get_value(current_row, current_col) != self._target_word[i]:
                return False
            
        return True


class CrossPatternSearchStrategy(GridSearchStrategy):
    def __init__(self, grid: 'Grid', direction_deltas: List[str], target_pattern: List[str]) -> None:
        self._grid = grid
        self._direction_deltas = direction_deltas
        self._target_pattern = target_pattern
        
        self._rows, self._cols = self._grid.get_size()
    
    def search(self) -> int:       
        occurrences = 0
        
        for row in range(self._rows):
            for col in range(self._cols):
                if self._is_cross_pattern_at_position(row, col):
                    occurrences += 1
                    
        return occurrences

    def _is_cross_pattern_at_position(self, row: int, col: int) -> bool:
        first_diagonal = self._get_diagonal_from_position(row, col, 1)
        second_diagonal = self._get_diagonal_from_position(row, col, -1)

        return first_diagonal in self._target_pattern and second_diagonal in self._target_pattern

    def _get_diagonal_from_position(self, row: int, col: int, direction_sign: int) -> List[str]:
        diagonal = []
        
        for delta in self._direction_deltas:
            current_row = row + delta
            current_col = col + direction_sign * delta
            
            if self._grid.is_valid_position(current_row, current_col):
                diagonal.append(self._grid.get_value(current_row, current_col))
                continue
            
            diagonal.append('')

        return diagonal
