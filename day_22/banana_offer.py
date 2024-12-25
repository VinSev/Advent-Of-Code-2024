from collections import defaultdict
from typing import List, Dict, Tuple
from operation import Operation


class BananaOffer:
    def __init__(self) -> None:
        self.banana_offer_sequences: defaultdict[Tuple[int], int] = defaultdict(int)

    def process_secret_number(self, secret_number: int) -> None:
        seen_sequences = set()
        price_changes: List[int] = []
        previous_last_digit = self.get_last_digit(secret_number)
        operation = Operation()

        for _ in range(2000):
            secret_number = operation.apply(secret_number)
            last_digit = self.get_last_digit(secret_number)
            self.process_price_change(price_changes, last_digit, previous_last_digit)
            sequence = self.get_sequence(price_changes)

            if sequence not in seen_sequences:
                seen_sequences.add(sequence)
                self.banana_offer_sequences[sequence] += last_digit

            previous_last_digit = last_digit

    def calculate_banana_offer_sequences(self, secret_numbers: List[int]) -> Dict[Tuple[int], int]:
        for secret_number in secret_numbers:
            self.process_secret_number(secret_number)
        return self.banana_offer_sequences

    @staticmethod
    def get_last_digit(number: int) -> int:
        return int(str(number)[-1])

    @staticmethod
    def calculate_price_change(previous_last_digit: int, last_digit: int) -> int:
        return previous_last_digit - last_digit

    @staticmethod
    def get_sequence(price_changes: List[int]) -> Tuple[int, int, int, int]:
        return tuple(price_changes[-4:])

    @staticmethod
    def process_price_change(price_changes: List[int], last_digit: int, previous_last_digit: int) -> None:
        price_change = BananaOffer.calculate_price_change(previous_last_digit, last_digit)
        price_changes.append(price_change)
