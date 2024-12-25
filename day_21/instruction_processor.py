from typing import List, TYPE_CHECKING

from keypad_factory import KeypadFactory
from sequence_finder import DFS

if TYPE_CHECKING:
    from keypad import Keypad


class InstructionProcessor():
    def __init__(self, instructions: List[str]) -> None:
        self.instructions = instructions

    def calculate_total_complexity(self, number_of_robots: int) -> int:
        numeric_robot_keypad = KeypadFactory().create_keypads(number_of_robots, DFS())

        total_complexity = 0

        for instruction in self.instructions:
            complexity = self.calculate_sequence_complexity(numeric_robot_keypad, instruction)
            total_complexity += complexity

        return total_complexity

    def calculate_sequence_complexity(self, 
                                      numeric_robot_keypad: 'Keypad', 
                                      instruction: str) -> int:
        numeric_keys = int(instruction[:3])
        length_shortest_sequence = numeric_robot_keypad.get_shortest_sequence_length(instruction)
        
        return numeric_keys * length_shortest_sequence