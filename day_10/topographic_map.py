from typing import List

from point import Point


class TopographicMap():
    def __init__(self, data: List[List[int]]):
        self.map = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def is_out_of_bounds(self, point: 'Point') -> bool:
        return point.x < 0 or point.y < 0 or point.x >= self.cols or point.y >= self.rows

    def get_height(self, point: 'Point') -> int:
        return self.map[point.y][point.x]
