from enum import Enum
from typing import List, Tuple

from point import Point


class TileType(Enum):
    GUARD = '^'
    OBSTRUCTION = '#'
    EMPTY = '.'


class TileMap():  
    def __init__(self, data: List[List[str]]):
        self._data = data
        self._rows = len(data)
        self._cols = len(data[0]) if self._rows > 0 else 0
    
    def size(self) -> Tuple[int, int]:
        return self._rows, self._cols

    def get_tile(self, point: 'Point') -> 'TileType':
        self._validate_bounds(point)
        
        return TileType(self._data[point.y][point.x])

    def set_tile(self, point: 'Point', tile_type: 'TileType') -> None:
        self._validate_bounds(point)
        self._data[point.y][point.x] = tile_type.value
        
    def get_tile_position(self, tile_type: 'TileType') -> 'Point':
        for row in range(self._rows):
            for col in range(self._cols):
                if self._data[row][col] == tile_type.value:
                    return Point(col, row)

        raise ValueError(f'Tile of type \'{tile_type.name}\' not found in the map.')
    
    def is_out_of_bounds(self, point: 'Point') -> bool:
        return point.x < 0 or point.y < 0 or point.x >= self._cols or point.y >= self._rows
    
    def _validate_bounds(self, point: 'Point') -> None:
        if self.is_out_of_bounds(point):
            raise ValueError(f'Tile at position ({point.x}, {point.y}) is out of bounds.')
