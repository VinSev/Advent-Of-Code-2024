from abc import ABC, abstractmethod
from collections import deque
from typing import Dict

from maze import Maze
from point import Point


class MazeSearchStrategy(ABC):
    @abstractmethod
    def search(self, maze: 'Maze') -> Dict['Point', int]:
        raise NotImplementedError
    
class BFS(MazeSearchStrategy):
    def search(self, maze: 'Maze') -> Dict['Point', int]:
        distance_map = {maze.start: 0}
        queue = deque([maze.start])
        
        while queue:
            current_position = queue.popleft()
            
            if current_position == maze.end:
                return distance_map
            
            current_distance = distance_map[current_position]
            
            for neighbor in maze.path_graph[current_position]:
                if neighbor not in distance_map:
                    queue.append(neighbor)
                    distance_map[neighbor] = current_distance + 1
                    
        return distance_map
    