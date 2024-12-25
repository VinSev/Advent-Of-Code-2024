import heapq as h
from typing import List, Tuple, Dict, Set

from point import Point
from maze import Maze

START = 'S'
END = 'E'
WALL = '#'
EMPTY = '.'

MOVE_COST = 1
ROTATE_COST = 1000


class MazeSolver:
    def __init__(self, maze: Maze) -> None:
        self.maze = maze
        self.lowest_cost: float = float('inf')
        self.end_indices: List[int] = []
        self.previous_steps: List[Tuple[int, Point]] = [(-1, Point(-1, -1))]

    def search(self) -> Tuple[float, List[int], List[Tuple[int, Point]]]:
        priority_queue: List[Tuple[int, int, Point, Point]] = [(0, 0, self.maze.start, Point(0, 1))]
        seen_costs: Dict[Tuple[Point, Point], float] = dict()

        while True:
            current_cost, index, current_position, current_direction = h.heappop(priority_queue)

            if current_cost > self.lowest_cost:
                break

            if current_position == self.maze.end:
                if current_cost < self.lowest_cost:
                    self.lowest_cost = current_cost
                    self.end_indices.clear()
                self.end_indices.append(index)
                continue

            if seen_costs.get((current_position, current_direction), float('inf')) < current_cost:
                continue
            
            seen_costs[(current_position, current_direction)] = current_cost

            self.move_forward(current_cost, index, current_position, current_direction, priority_queue)
            self.rotate_and_push_new_directions(current_cost, index, current_position, current_direction, priority_queue)

        return self.lowest_cost, self.end_indices, self.previous_steps

    def move_forward(self, cost: int, index: int, position: Point, direction: Point, priority_queue: List[Tuple[int, int, Point, Point]]):
        next_point = position.move(direction)
        
        if self.maze.grid[next_point.x][next_point.y] == EMPTY:
            h.heappush(priority_queue, (cost + MOVE_COST, len(self.previous_steps), next_point, direction))
            self.previous_steps.append((index, position))

    def rotate_and_push_new_directions(self, cost: int, index: int, position: Point, direction: Point, priority_queue: List[Tuple[int, int, Point, Point]]):
        for new_direction in Maze.DIRECTIONS:
            if (new_direction.x, new_direction.y) != (-direction.x, -direction.y):
                h.heappush(priority_queue, (cost + ROTATE_COST, len(self.previous_steps), position, new_direction))
                self.previous_steps.append((index, position))

    def backtrack_to_find_visited_positions(self, end_indices: List[int]) -> Set[Point]:
        visited_positions: Set[Point] = set()
        
        for index in end_indices:
            current_point = self.maze.end
            
            while index != -1:
                visited_positions.add(current_point)
                index, current_point = self.previous_steps[index]

        return visited_positions
