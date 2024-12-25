from typing import Dict, ItemsView, List


class StoneInventory:
    def __init__(self) -> None:
        self._stone_dict: Dict[int, int] = {}

    def _update_stone(self, stone: int, count: int) -> None:
        if stone in self._stone_dict:
            self._stone_dict[stone] += count
            return
        
        self._stone_dict[stone] = count

    def update_stones(self, stones: List[int], count: int) -> None:
        for stone in stones:
            self._update_stone(stone, count)
            
    def clear(self) -> None:
        self._stone_dict.clear()
            
    def items(self) -> ItemsView[int, int]:
        return self._stone_dict.items()
            
    def sum_inventory(self) -> int:
        return sum(self._stone_dict.values())
