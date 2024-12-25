from typing import Set

from direction import Direction
from guard import Guard
from point import Point
from tile_map import TileMap, TileType


class Patrol:
    def __init__(self, tile_map: 'TileMap', start_position: 'Point'):
        self._tile_map = tile_map
        self._start_position = start_position
        
        self._guard = Guard(tile_map)
        self._visited_positions = set()

    def get_visited_positions(self) -> Set['Point']:
        guard_position = self._start_position
        direction = Direction.UP

        while not self._tile_map.is_out_of_bounds(guard_position):
            self._visited_positions.add(guard_position)
            guard_position, direction = self._guard.move(guard_position, direction)

        return self._visited_positions

    def find_loop_positions(self) -> Set['Point']:
        loop_positions = set()

        for position in self._visited_positions:
            self._tile_map.set_tile(position, TileType.OBSTRUCTION)
            
            if self._check_for_loop():
                loop_positions.add(position)

            self._tile_map.set_tile(position, TileType.EMPTY)  

        return loop_positions
    
    def _check_for_loop(self) -> bool:
        seen_states = set()
        guard_position = self._start_position
        direction = Direction.UP

        while not self._tile_map.is_out_of_bounds(guard_position):
            current_state = (guard_position.x, guard_position.y, direction.value.x, direction.value.y)
            
            if current_state in seen_states:
                return True
            
            seen_states.add(current_state)
            guard_position, direction = self._guard.move(guard_position, direction)

        return False
