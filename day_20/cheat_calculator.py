from typing import Dict, List, Tuple

from maze import Maze
from maze_search_strategy import MazeSearchStrategy
from point import Point


class CheatCalculator():
    def __init__(
            self, 
            maze: 'Maze', 
            search_algorithm: 'MazeSearchStrategy'
        ) -> None:
        self._maze = maze
        self._search_algorithm = search_algorithm

    def _generate_deltas(
            self, 
            max_distance: int
        ) -> List['Point']:
        deltas = []
        
        for dy in range(-max_distance, max_distance + 1):
            for dx in range(-max_distance, max_distance + 1):
                distance = abs(dx) + abs(dy)
                
                if distance <= max_distance:
                    delta = Point(dx, dy)
                    deltas.append(delta)
                    
        return deltas

    def _calculate_cheats(
            self, 
            distance_map: Dict['Point', int], 
            deltas: List['Point']
        ) -> Dict[Tuple['Point', 'Point'], int]:
        cheat_counts = {}
        
        for position, current_distance in distance_map.items():
            for delta in deltas:
                new_position = position + delta
                new_distance = distance_map.get(new_position)
                delta_distance = abs(delta.x) + abs(delta.y)
                
                if new_distance is not None:
                    cheat_value = current_distance - delta_distance - new_distance
                    cheat_counts[(position, new_position)] = cheat_value
                    
        return cheat_counts

    def get_cheats_exceeding_threshold(
            self, 
            threshold: int, 
            max_cheat_distance: int
        ) -> int:
        distance_map = self._search_algorithm.search(self._maze)
        deltas = self._generate_deltas(max_cheat_distance)
        cheat_counts = self._calculate_cheats(distance_map, deltas)
        
        return sum(1 for value in cheat_counts.values() if value >= threshold)
    