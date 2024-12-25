from collections import deque
from typing import List, Optional, Tuple

from file_reader import FileReader


class DiskMapParser:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._disk_map = []
        self._file_start_indices = deque()

    def parse(self) -> Tuple[List[Optional[int]], deque]:
        disk_map = self._read_disk_map()
        self._transform_disk_map(disk_map)
        
        return self._disk_map, self._file_start_indices

    def _read_disk_map(self) -> List[int]:
        return FileReader.read_matrix(self._file_path, target_type=int, separator='')[0]

    def _transform_disk_map(self, disk_map: List[int]) -> None:
        is_file = True
        file_id = 0
        
        for space in disk_map:
            start = len(self._disk_map)
            value = file_id if is_file else None
            self._disk_map.extend([value] * space)
            
            if is_file:
                self._file_start_indices.append(start)
                file_id += 1
            
            is_file = not is_file
