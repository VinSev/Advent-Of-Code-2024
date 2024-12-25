from typing import Tuple

from direction import Direction
from point import Point
from tile_map import TileMap, TileType


class Guard:
    def __init__(self, tile_map: 'TileMap'):
        self._tile_map = tile_map
        
        self._directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]

    def move(self, position: 'Point', direction: 'Direction') -> Tuple['Point', 'Direction']:
        new_position = position + direction.value
        
        if self._tile_map.is_out_of_bounds(new_position) or self._tile_map.get_tile(new_position) != TileType.OBSTRUCTION:
            return new_position, direction
        
        current_index = self._directions.index(direction)
        new_index = (current_index + 1) % len(self._directions)
        
        return position, self._directions[new_index]
