from abc import ABC, abstractmethod
from typing import Set

from point import Point


class AntinodeCalculator(ABC):
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self._num_rows = num_rows
        self._num_cols = num_cols
        
    @abstractmethod
    def calculate(self, point1: 'Point', point2: 'Point') -> Set['Point']:
        raise NotImplementedError
    
    def _is_out_of_bounds(self, point: Point) -> bool:
        return point.x < 0 or point.y < 0 or point.x >= self._num_rows or point.y >= self._num_cols


class FixedDistanceAntinodeCalculator(AntinodeCalculator):
    def calculate(self, point1: 'Point', point2: 'Point') -> Set['Point']:
        antinodes = set()

        point = point1 + (point1 - point2)
        
        if not self._is_out_of_bounds(point):
            antinodes.add(point)
            
        return antinodes

 
class ContinuousAntinodeCalculator(AntinodeCalculator):
    def calculate(self, point1: Point, point2: Point) -> Set[Point]:
        antinodes = set()

        delta_point = point1 - point2

        point = point1
        
        while not self._is_out_of_bounds(point):
            antinodes.add(point)
            point += delta_point
            
        return antinodes
