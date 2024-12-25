from typing import List

from point import Point


START = 'S'
END = 'E'
WALL = '#'
EMPTY = '.'

DIRECTIONS = (Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0))


class Maze():
    def __init__(self, maze: List[List[str]]) -> None:
        self.maze = maze
        self.path_graph = {}
        
        self.start = None
        self.end = None
        
        self._build_path_graph()
        self._locate_start_and_end()

    def is_out_of_bounds(self, position: 'Point') -> bool:
        return (position.x < 0 or position.y < 0 or 
                position.x >= len(self.maze[0]) or position.y >= len(self.maze))

    def is_valid(self, position: 'Point') -> bool:
        return (not self.is_out_of_bounds(position) and 
                self.maze[position.y][position.x] != WALL)

    def _create_path_node(self, position: 'Point') -> None:
        self.path_graph[position] = []
        
        for direction in DIRECTIONS:
            neighbor = position + direction
            
            if self.is_valid(neighbor):
                self.path_graph[position].append(neighbor)

    def _build_path_graph(self) -> None:
        for y, line in enumerate(self.maze):
            for x, value in enumerate(line):
                if value != WALL:
                    self._create_path_node(Point(x, y))

    def _locate_start_and_end(self) -> None:
        for y, line in enumerate(self.maze):
            for x, value in enumerate(line):
                if value == START:
                    self.start = Point(x, y)
                elif value == END:
                    self.end = Point(x, y)
                    
                if self.start and self.end:
                    return
                
        raise ValueError('No start and/or end found in the maze')
    