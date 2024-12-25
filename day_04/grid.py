from typing import List, Tuple


class Grid():  
    def __init__(self, data: List[List[str]]) -> None:
        self._data = data
        self._rows = len(data)
        self._cols = len(data[0]) if data else 0
        
    def get_value(self, row: int, col: int) -> str:
        if self.is_valid_position(row, col):
            return self._data[row][col]
        
        return None
    
    def get_size(self) -> Tuple[int, int]:
        return self._rows, self._cols

    def is_valid_position(self, row: int, col: int) -> bool:
        return 0 <= row < self._rows and 0 <= col < self._cols
