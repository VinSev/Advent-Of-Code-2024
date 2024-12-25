from file_reader import FileReader
from instruction_processor import InstructionProcessor


def main() -> None:
    instructions = FileReader.read_lines('data.txt')

    processor = InstructionProcessor(instructions)

    total_complexity = processor.calculate_total_complexity(number_of_robots=2)
    print(f'Complexity (2 Robots):\t{total_complexity}')

    total_complexity = processor.calculate_total_complexity(number_of_robots=25)
    print(f'Complexity (25 Robots):\t{total_complexity}')


if __name__ == '__main__':
    main()
