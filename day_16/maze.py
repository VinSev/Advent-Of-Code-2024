from point import Point
from typing import List, Tuple, Optional

START = 'S'
END = 'E'
WALL = '#'
EMPTY = '.'

MOVE_COST = 1
ROTATE_COST = 1000


class Maze:
    DIRECTIONS: List[Point] = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]

    def __init__(self, file_path: str) -> None:
        self.grid: List[List[str]] = self.read_maze(file_path)
        self.start: Optional[Point] = None
        self.end: Optional[Point] = None
        self.start, self.end = self.locate_start_and_end()

    def read_maze(self, file_path: str) -> List[List[str]]:
        with open(file_path) as file:
            content = file.read()
        return [[character for character in line] for line in content.splitlines()]

    def locate_start_and_end(self) -> Tuple[Optional[Point], Optional[Point]]:
        start: Optional[Point] = None
        end: Optional[Point] = None
        
        for x, row in enumerate(self.grid):
            for y, character in enumerate(row):
                if character == START:
                    start = Point(x, y)
                    self.grid[x][y] = EMPTY
                elif character == END:
                    end = Point(x, y)
                    self.grid[x][y] = EMPTY
                    
        return start, end
