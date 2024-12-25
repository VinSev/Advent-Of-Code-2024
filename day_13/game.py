from typing import List, Tuple

from point import Point


class Game():
    def are_valid_presses(self, presses: float) -> bool:
        return presses >= 0 and presses.is_integer()

    def calculate_button_presses(self, button_a: 'Point', button_b: 'Point', prize_position: 'Point') -> Tuple[int, int]:
        delta = button_a.x * button_b.y - button_a.y * button_b.x

        a_presses = ((prize_position.x * button_b.y) - (prize_position.y * button_b.x)) / delta
        b_presses = ((prize_position.y * button_a.x) - (prize_position.x * button_a.y)) / delta

        if not self.are_valid_presses(a_presses) or not self.are_valid_presses(b_presses):
            return (0, 0)

        return (int(a_presses), int(b_presses))

    def calculate_total_tokens(self, claw_machines: List[List['Point']], offset: int = 0) -> int:
        total_tokens = 0

        for claw_machine in claw_machines:
            button_a, button_b, prize_position = claw_machine
            adjusted_prize_position = prize_position + Point(offset, offset)
            
            a_presses, b_presses = self.calculate_button_presses(button_a, button_b, adjusted_prize_position)
            total_tokens += (a_presses * 3) + b_presses

        return total_tokens
