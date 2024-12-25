from region_finder import RegionFinder
from typing import List, Tuple


class GardenMapProcessor():
    def __init__(self, garden_map: List[List[str]]) -> None:
        self._garden_map = garden_map
        self._region_finder = RegionFinder(self._garden_map)
        
    def get_region_data(self) -> List[Tuple[List[Tuple[int, int]], int, int]]:
        regions = []
        
        for y in range(len(self._garden_map)):
            for x in range(len(self._garden_map[0])):
                plant_type = self._garden_map[y][x]
                
                positions, perimeter = self._region_finder.flood_fill(x, y, plant_type)
                sides = self._region_finder.count_sides(positions)
                
                regions.append((positions, perimeter, sides))
        
        return regions
