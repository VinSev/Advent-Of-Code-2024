from typing import List

from stone_inventory import StoneInventory
from stone_transformer import StoneTransformer


class BlinkProcessor:
    def __init__(self) -> None:
        self._stone_inventory = StoneInventory()

    def _process_blink(self) -> None:
        new_inventory = StoneInventory()
        
        for stone, count in self._stone_inventory.items():
            results = StoneTransformer(stone).transform()
            new_inventory.update_stones(results, count)
        
        self._stone_inventory = new_inventory

    def process_blinks(self, stones: List[int], blinks: int) -> int:
        self._stone_inventory.clear()
        self._stone_inventory.update_stones(stones, 1)
        
        for _ in range(blinks):
            self._process_blink()
        
        return self._stone_inventory.sum_inventory()
