from typing import List, Union


class StoneTransformer:
    def __init__(self, stone: int) -> None:
        self._stone = stone
        
    def transform(self) -> List[Union[int, List[int]]]:
        if self._stone == 0:
            return [1]
        
        if len(str(self._stone)) % 2 == 0:
            middle = len(str(self._stone)) // 2
            
            left = int(str(self._stone)[:middle])
            right = int(str(self._stone)[middle:])
            
            return [left, right]

        return [self._stone * 2024]
