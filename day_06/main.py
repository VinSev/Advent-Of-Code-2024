from file_reader import FileReader
from patrol import Patrol
from tile_map import TileMap, TileType


def main() -> None:
    tile_map_data = FileReader.read_matrix('data.txt', separator='')
    tile_map = TileMap(tile_map_data)

    guard_position = tile_map.get_tile_position(TileType.GUARD)
    
    patrol = Patrol(tile_map, guard_position)

    visited_positions = patrol.get_visited_positions()
    print(f'Patrol Area: {len(visited_positions)}')

    loop_positions = patrol.find_loop_positions()
    print(f'Loop Positions: {len(loop_positions)}')


if __name__ == '__main__':
    main()
