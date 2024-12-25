from typing import List, Tuple, Optional
from banana_offer import BananaOffer
from operation import Operation


class BananaCalculator:
    def __init__(self) -> None:
        self.operation = Operation()
        self.banana_offer = BananaOffer()

    def calculate_total_banana_sum(self, secret_numbers: List[int]) -> int:
        total_sum = 0
        for secret_number in secret_numbers:
            for _ in range(2000):
                secret_number = self.operation.apply(secret_number)
            total_sum += secret_number
        return total_sum

    def find_best_banana_offer_sequence(self, secret_numbers: List[int]) -> Tuple[Optional[Tuple[int]], int]:
        banana_offer_sequences = self.banana_offer.calculate_banana_offer_sequences(secret_numbers)
        best_sequence = None
        max_bananas = 0

        for sequence, bananas in banana_offer_sequences.items():
            if bananas > max_bananas:
                best_sequence = sequence
                max_bananas = bananas

        return best_sequence, max_bananas
