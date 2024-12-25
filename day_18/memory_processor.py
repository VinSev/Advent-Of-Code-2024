from collections import deque
from typing import List

from direction import DIRECTIONS
from memory_type import MemoryType
from point import Point


class MemoryProcessor():
    def __init__(self, memory: List[List[str]], falling_bytes: List['Point'], start: 'Point', exit: 'Point') -> None:
        self._memory = memory
        self._falling_bytes = falling_bytes
        self._start = start
        self._current_position = self._start
        self._exit = exit
        
        self._n_rows = len(self._memory)
        self._n_cols = len(self._memory[0])
        
    def _is_out_of_bounds(self, position: 'Point') -> bool:
        return position.x < 0 or position.y < 0 or position.x >= self._n_cols or position.y >= self._n_rows

    def _is_valid(self, position: 'Point') -> bool:
        return not self._is_out_of_bounds(position) and self._memory[position.y][position.x] == MemoryType.SAFE

    def min_steps_to_exit(self) -> int:
        queue = deque([self._start])
        visited = set()
        visited.add(self._start)
        
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                self._current_position = queue.popleft()
                
                if self._current_position == self._exit:
                    return steps
                
                for direction in DIRECTIONS:      
                    next_position = self._current_position.move(direction.value)
                    
                    if self._is_valid( next_position) and next_position not in visited:
                        visited.add(next_position)
                        queue.append(next_position)
            
            steps += 1
        
        return -1

    def corrupt_memory(self, byte_amount: int) -> None:
        for falling_byte in self._falling_bytes[:byte_amount]:
            self._memory[falling_byte[1]][falling_byte[0]] = MemoryType.CORRUPTED


    def reset_memory(self, byte_amount: int) -> None:
        for falling_byte in self._falling_bytes[:byte_amount]:
            self._memory[falling_byte[1]][falling_byte[0]] = MemoryType.SAFE
            
    def first_blocking_byte(self) -> 'Point':
        low, high = 0, len(self._falling_bytes) - 1
        first_blocking_byte_position = None

        while low <= high:
            middle = (low + high) // 2
            
            self.corrupt_memory(middle + 1)
            
            if self.min_steps_to_exit() == -1:
                first_blocking_byte_position = self._falling_bytes[middle]
                high = middle - 1
            else:
                low = middle + 1
            
            self.reset_memory(middle + 1)
            
        return Point(*first_blocking_byte_position)
