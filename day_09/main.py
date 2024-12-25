from typing import List, Optional

from disk_map_parser import DiskMapParser
from sort_strategy import SortByFile, SortBySpace


def calculate_checksum(disk_map: List[Optional[int]]) -> int:
    return sum(i * space for i, space in enumerate(disk_map) if isinstance(space, int))

def main() -> None:
    disk_map_parser = DiskMapParser('data.txt')
    unordered_disk_map, file_start_indices = disk_map_parser.parse()
    
    ordered_disk_map_spaces = SortBySpace(unordered_disk_map.copy()).sort()
    checksum_spaces = calculate_checksum(ordered_disk_map_spaces)
    print('Checksum (Spaces):', checksum_spaces)

    ordered_disk_map_files = SortByFile(unordered_disk_map.copy(), file_start_indices.copy()).sort()
    checksum_files = calculate_checksum(ordered_disk_map_files)
    print('Checksum (Files):', checksum_files )


if __name__ == '__main__':
    main()
