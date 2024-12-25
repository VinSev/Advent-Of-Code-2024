from typing import List, TYPE_CHECKING

from key_constants import UP, RIGHT, DOWN, LEFT, START, EMPTY
from keypad import Keypad, HumanControlledKeypad, RobotControlledKeypad

if TYPE_CHECKING:
    from sequence_finder import SequenceFinder


NUMERIC_KEYPAD = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [EMPTY, '0', START]]
DIRECTIONAL_KEYPAD = [[EMPTY, UP, START], [LEFT, DOWN, RIGHT]]


class KeypadFactory():
    @staticmethod
    def create_keypads(number_of_robots: int, 
                       search_strategy: 'SequenceFinder') -> Keypad:
        human_keypad = KeypadFactory.create_human_keypad(None, DIRECTIONAL_KEYPAD, search_strategy)
        robot_keypad = human_keypad

        for _ in range(number_of_robots):
            robot_keypad = KeypadFactory.create_robot_keypad(robot_keypad, DIRECTIONAL_KEYPAD, search_strategy)

        return KeypadFactory.create_robot_keypad(robot_keypad, NUMERIC_KEYPAD, search_strategy)

    @staticmethod
    def create_human_keypad(linked_keypad: Keypad, 
                            keypad_layout: List[List[str]], 
                            search_strategy: 'SequenceFinder') -> HumanControlledKeypad:
        return HumanControlledKeypad(linked_keypad, keypad_layout, search_strategy)

    @staticmethod
    def create_robot_keypad(linked_keypad: Keypad, 
                            keypad_layout: List[List[str]], 
                            search_strategy: 'SequenceFinder') -> RobotControlledKeypad:
        return RobotControlledKeypad(linked_keypad, keypad_layout, search_strategy)
