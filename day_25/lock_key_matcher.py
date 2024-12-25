from typing import List, Set, Tuple

from schematic import Schematic


class LockKeyMatcher:
    def __init__(self, locks: List[Schematic], keys: List[Schematic]) -> None:
        self.locks = locks
        self.keys = keys

    def get_unique_lock_key_pairs(self) -> Set[Tuple[int, int]]:
        unique_pairs = set()

        for i, lock in enumerate(self.locks):
            lock_heights = lock.get_pin_heights()
            for j, key in enumerate(self.keys):
                key_heights = key.get_pin_heights()
                fits = True
                
                for lock_height, key_height in zip(lock_heights, key_heights):
                    if lock_height + key_height > 5:
                        fits = False
                        break
                
                if fits:
                    unique_pairs.add((i, j))
                    
        return unique_pairs
