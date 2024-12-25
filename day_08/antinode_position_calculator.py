import itertools
from typing import Dict, List, Set

from antinode_calculator import AntinodeCalculator
from point import Point


class AntinodePositionCalculator:
    def __init__(self, antenna_map: List[List[str]], antinode_calculator: 'AntinodeCalculator') -> None:
        self._antenna_positions = self._parse_antenna_positions(antenna_map)
        self._antinode_calculator = antinode_calculator

    def _parse_antenna_positions(self, antenna_map: List[List[str]]) -> Dict[str, List['Point']]:
        antenna_positions = {}
        
        for i, row in enumerate(antenna_map):
            for j, frequency in enumerate(row):
                if frequency != '.':
                    if frequency not in antenna_positions:
                        antenna_positions[frequency] = []
                        
                    antenna_positions[frequency].append(Point(i, j))
                    
        return antenna_positions
    
    def set_antinode_calculator(self, antitinode_calculator: 'AntinodeCalculator') -> None:
        self._antinode_calculator = antitinode_calculator

    def calculate_antinode_positions(self) -> Set['Point']:
        antinodes = set()

        for positions in self._antenna_positions.values():
            for point1, point2 in itertools.combinations(positions, 2):
                antinodes |= self._antinode_calculator.calculate(point1, point2)
                antinodes |= self._antinode_calculator.calculate(point2, point1)

        return antinodes
