import re
from typing import List

from robot import Robot


class Simulation():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        
        self.spaces = self.initialize_spaces()
        self.robots: List[Robot] = []

    def initialize_spaces(self) -> List[List[int]]:
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def read_robot_data(self, file_path: str) -> None:
        with open(file_path, 'r') as file:
            content = file.read()

        for robot in content.splitlines():
            digits = [int(value) for value in re.findall(r'\d+|-\d+', robot)]
            self.robots.append(Robot((digits[0], digits[1]), (digits[2], digits[3])))

    def simulate_robot_movement(self, seconds: int) -> None:
        for _ in range(1, seconds + 1):
            for robot in self.robots:
                robot.move(self.spaces, self.width, self.height)

    def calculate_quadrants(self) -> List[int]:
        middle_x = self.width // 2
        middle_y = self.height // 2
        quadrants = [0, 0, 0, 0]

        for x in range(self.width):
            for y in range(self.height):
                if x < middle_x and y < middle_y:
                    quadrants[0] += self.spaces[y][x]
                elif x > middle_x and y < middle_y:
                    quadrants[1] += self.spaces[y][x]
                elif x < middle_x and y > middle_y:
                    quadrants[2] += self.spaces[y][x]
                elif x > middle_x and y > middle_y:
                    quadrants[3] += self.spaces[y][x]

        return quadrants

    def calculate_security_factor(self, quadrants: List[int]) -> int:
        security_factor = 1
        
        for count in quadrants:
            security_factor *= count
            
        return security_factor
