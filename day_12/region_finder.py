from typing import List, Tuple

from direction import Direction, DIRECTIONS


class RegionFinder():
    def __init__(self, garden_map: List[List[str]]) -> None:
        self._garden_map = garden_map
        self._visited = set()
        self._n_rows = len(self._garden_map)
        self._n_cols = len(self._garden_map[0])
        
    def _is_out_of_bounds(self, x: int, y: int) -> bool:
        return x < 0 or y < 0 or x >= self._n_cols or y >= self._n_rows

    def flood_fill(self, x: int, y: int, plant_type: str) -> Tuple[List[Tuple[int, int]], int]:
        if self._is_out_of_bounds(x, y) or (x, y) in self._visited or self._garden_map[y][x] != plant_type:
            return [], 0

        self._visited.add((x, y))
        positions = [(x, y)]
        perimeter = 0

        for direction in DIRECTIONS:
            nx, ny = direction.move(x, y)
            
            if self._is_out_of_bounds(nx, ny) or self._garden_map[ny][nx] != plant_type:
                perimeter += 1
                continue

            new_positions, new_perimeter = self.flood_fill(nx, ny, plant_type)
            positions.extend(new_positions)
            perimeter += new_perimeter

        return positions, perimeter

    def _find_end_of_side(self, positions: List[Tuple[int, int]], x: int, y: int, direction: Direction) -> Tuple[int, int]:
        dx, dy = direction.value
        
        while (x + dy, y + dx) in positions and (x + dx, y + dy) not in positions:
            x += dy
            y += dx
            
        return x, y

    def count_sides(self, positions: List[Tuple[int, int]]) -> int:
        visited = set()
        total_sides = 0
        
        for x, y in positions:
            for direction in DIRECTIONS:
                nx, ny = direction.move(x, y)
                
                if (nx, ny) not in positions:
                    end_x, end_y = self._find_end_of_side(positions, x, y, direction)
                    
                    if (end_x, end_y, direction) not in visited:
                        visited.add((end_x, end_y, direction))
                        total_sides += 1

        return total_sides
