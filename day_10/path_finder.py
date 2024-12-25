from collections import deque
from direction import Direction
from point import Point
from topographic_map import TopographicMap
from typing import Dict, Tuple


MAX_HEIGHT = 9


class Pathfinder():
    def __init__(self, topographic_map: 'TopographicMap'):
        self._topographic_map = topographic_map
        
    def find_paths(self, start: 'Point') -> Tuple[int, int]:
        queue = deque([start])
        
        visited = {
            start: 1
        }
        
        total_score = 0
        total_rating = 0

        while queue:
            current_point = queue.popleft()
            current_height = self._topographic_map.get_height(current_point)

            if current_height == MAX_HEIGHT:
                total_score, total_rating = self._update_score_and_rating(visited, total_score, total_rating, current_point)
                continue
            
            visited = self._explore_neighbors(queue, visited.copy(), current_point, current_height)

        return total_score, total_rating

    def _update_score_and_rating(self, visited: Dict['Point', int], total_score: int, total_rating: int, current_point: 'Point') -> Tuple[int, int]:
        total_score += 1
        total_rating += visited[current_point]
        
        return total_score, total_rating

    def _explore_neighbors(self, queue: deque, visited: Dict['Point', int], current_point: 'Point', current_height: int) -> Dict['Point', int]:
        for direction in Direction:
            neighbor_point = direction.move(current_point)

            if (not self._topographic_map.is_out_of_bounds(neighbor_point) and
                self._is_valid_move(current_height, self._topographic_map.get_height(neighbor_point))):
                
                if neighbor_point not in visited:
                    queue.append(neighbor_point)
                    visited[neighbor_point] = 0
                    
                visited[neighbor_point] += visited[current_point]
        
        return visited

    def _is_valid_move(self, current_height: int, neighbor_height: int) -> bool:
        return neighbor_height == current_height + 1
    