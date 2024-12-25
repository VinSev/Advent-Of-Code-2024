from re import findall

from debugger import Debugger
from initial_value_finder import InitialValueFinder


def main() -> None:
    with open('data.txt', 'r') as file:
        content = [int(n) for n in findall(r'\d+', file.read())]

    initial_a, _, _, *program_data = content

    debugger = Debugger(program_data, initial_a)
    joined_debugger_results = ','.join(str(digit) for digit in debugger.run())
    print(f'Debugger results: {joined_debugger_results}')

    target_output = program_data[::-1]
    lowest_inital_a = InitialValueFinder.get_lowest_initial_a(program_data, target_output=target_output)
    print(f'Lowest initial value for Register A: {lowest_inital_a}')


if __name__ == '__main__':
    main()
