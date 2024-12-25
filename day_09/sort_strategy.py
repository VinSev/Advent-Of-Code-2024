from abc import ABC, abstractmethod
from collections import deque
from typing import List, Optional


class SortStrategy(ABC):
    @abstractmethod
    def sort(self) -> List[Optional[int]]:
        pass


class SortBySpace(SortStrategy):
    def __init__(self, disk_map: List[Optional[int]]) -> None:
        self._disk_map = disk_map
        
    def sort(self) -> List[Optional[int]]:
        left, right = 0, len(self._disk_map) - 1
        
        while left < right:
            while left < right and self._disk_map[right] is None:
                right -= 1
                
            while left < right and isinstance(self._disk_map[left], int):
                left += 1
                
            if left < right:
                self._swap_space(left, right)

        return self._disk_map
    
    def _swap_space(self, left, right) -> None:
        temp = self._disk_map[left]
        self._disk_map[left] = self._disk_map[right]
        self._disk_map[right] = temp


class SortByFile(SortStrategy):
    def __init__(self, disk_map: List[Optional[int]], file_start_indices: deque) -> None:
        self._disk_map = disk_map
        self._file_start_indices = file_start_indices
        
    def sort(self) -> List[Optional[int]]:
        while self._file_start_indices:
            file_start = self._file_start_indices.pop()
            file_id = self._disk_map[file_start]
            
            file_end = self._find_file_end(file_start, file_id)
            target_gap_length = file_end - file_start + 1
            
            gap_start = self._find_left_most_gap(target_gap_length)
            
            if gap_start is not None and gap_start < file_start:
                self._swap_file(target_gap_length, gap_start, file_start, file_id)

        return self._disk_map
    
    def _swap_file(self, gap_length: int, gap_start: int, file_start: int, file_id: int) -> None:
        for i in range(gap_length):
            self._disk_map[gap_start + i] = file_id
            self._disk_map[file_start + i] = None
            
    def _find_left_most_gap(self, target_gap_length: int) -> Optional[int]:
        current_gap_length = 0

        for i in range(len(self._disk_map)):
            if self._disk_map[i] is not None:
                current_gap_length = 0
                continue
            
            current_gap_length += 1
            
            if current_gap_length == target_gap_length:
                return i - target_gap_length + 1

        return None

    def _find_file_end(self, file_start: int, file_id: int) -> int:
        for file_end in range(file_start, len(self._disk_map)):
            if self._disk_map[file_end] != file_id:
                return file_end - 1
            
        return len(self._disk_map) - 1    
    