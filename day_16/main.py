from maze import Maze
from maze_solver import MazeSolver


def main() -> None:
    maze = Maze('data.txt')
    solver = MazeSolver(maze)
    lowest_cost, end_indices, _ = solver.search()
    visited_positions = solver.backtrack_to_find_visited_positions(end_indices)

    print(f'Lowest score: {lowest_cost}')
    print(f'Tile count: {len(visited_positions)}')

if __name__ == '__main__':
    main()
