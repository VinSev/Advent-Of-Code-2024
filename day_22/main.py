from banana_calculator import BananaCalculator


def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read()

    secret_numbers = [int(secret_number) for secret_number in content.splitlines()]
    
    calculator = BananaCalculator()

    total_bananas = calculator.calculate_total_banana_sum(secret_numbers)
    print(f'Total banana sum: {total_bananas}')

    _, max_bananas = calculator.find_best_banana_offer_sequence(secret_numbers)
    print(f'Most bananas earned: {max_bananas}')


if __name__ == '__main__':
    main()
