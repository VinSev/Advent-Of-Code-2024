from typing import List


FILLED = '#'
EMPTY = '.'


class Schematic:
    def __init__(self, schematic: List[List[str]]):
        self.schematic = schematic
        
    def get_pin_heights(self) -> List[int]:
        heights = []
        num_columns = len(self.schematic[0])
        
        if not self.is_lock():
            self.schematic.reverse()

        for col in range(num_columns):
            height = 0
            
            for row in range(1, len(self.schematic) - 1):
                if self.schematic[row][col] == EMPTY:
                    break

                height += 1

            heights.append(height)

        return heights
    
    def is_lock(self) -> bool:
        return all(value == FILLED for value in self.schematic[0])
