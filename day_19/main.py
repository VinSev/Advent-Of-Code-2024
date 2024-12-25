from towel_processor import TowelProcessor


def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read()

    towel_patterns = set(content.split('\n\n')[0].split(', '))
    desired_designs = [line for line in content.split('\n\n')[1].splitlines()]

    towel_processor = TowelProcessor()
    possible_arrangement_counts = [
        towel_processor.count_possible_towel_arrangements(towel_patterns, design) 
        for design in desired_designs
    ]

    constructible_design_count = sum(1 for count in possible_arrangement_counts if count != 0)
    print(f'Amount constructible designs: {constructible_design_count}')

    total_arrangement_count = sum(possible_arrangement_counts)
    print(f'Total possible arrangements: {total_arrangement_count}')
    

if __name__ == '__main__':
    main()
