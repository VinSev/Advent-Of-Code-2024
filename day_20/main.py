from cheat_calculator import CheatCalculator
from maze import Maze
from maze_search_strategy import BFS


def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read()
        
    maze_data = [[value for value in line] for line in content.splitlines()]
    maze = Maze(maze_data)

    search_algorithm = BFS()
    cheat_calculator = CheatCalculator(maze, search_algorithm)
    
    cheats_exceeding_threshold = cheat_calculator.get_cheats_exceeding_threshold(
        threshold=100, 
        max_cheat_distance=2
    )
    print(f'Cheats amount (with cheat distance 2): {cheats_exceeding_threshold}')

    cheats_exceeding_threshold = cheat_calculator.get_cheats_exceeding_threshold(
        threshold=100, 
        max_cheat_distance=20
    )
    print(f'Cheats amount (with cheat distance 20): {cheats_exceeding_threshold}')


if __name__ == '__main__':
    main()
