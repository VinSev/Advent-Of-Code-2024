from antinode_calculator import ContinuousAntinodeCalculator, FixedDistanceAntinodeCalculator
from antinode_position_calculator import AntinodePositionCalculator
from file_reader import FileReader


def main() -> None:
    antenna_map = FileReader.read_matrix('data.txt', separator='')

    num_rows = len(antenna_map)
    num_cols = len(antenna_map[0])

    fixed_calculator = FixedDistanceAntinodeCalculator(num_rows, num_cols)
    position_calculator = AntinodePositionCalculator(antenna_map, fixed_calculator)
    antinodes = position_calculator.calculate_antinode_positions()
    print(f'Fixed Distance Model: {len(antinodes)}')

    continuous_calculator = ContinuousAntinodeCalculator(num_rows, num_cols)
    position_calculator.set_antinode_calculator(continuous_calculator)
    antinodes = position_calculator.calculate_antinode_positions()
    print(f'Continuous Model: {len(antinodes)}')


if __name__ == '__main__':
    main()
