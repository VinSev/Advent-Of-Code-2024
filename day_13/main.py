import re

from game import Game
from point import Point


def main() -> None:
    claw_machines = []
    current_machine = []

    with open('data.txt', 'r') as file:
        content = file.read()
        
    for line in content.splitlines():
        if not line.strip():
            if current_machine:
                claw_machines.append(current_machine)
                current_machine = []
            continue

        position = re.findall(r'\d+', line)
        current_machine.append(Point(int(position[0]), int(position[1])))

    if current_machine:
        claw_machines.append(current_machine)

    game = Game()
    
    total_tokens = game.calculate_total_tokens(claw_machines)
    print(f'Total tokens (without offset): {total_tokens}')
    
    total_tokens = game.calculate_total_tokens(claw_machines, offset=10000000000000)
    print(f'Total tokens (with offset): {total_tokens}')

    
if __name__ == '__main__':
    main()
