from typing import List, Tuple


class Robot():
    def __init__(self, position: Tuple[int, int], velocity: Tuple[int, int]) -> None:
        self.position = position
        self.velocity = velocity

    def move(self, spaces: List[List[int]], width: int, height: int) -> None:
        x, y = self.position
        spaces[y][x] = max(spaces[y][x] - 1, 0)

        new_x = (x + self.velocity[0]) % width
        new_y = (y + self.velocity[1]) % height

        self.position = (new_x, new_y)
        spaces[new_y][new_x] += 1
