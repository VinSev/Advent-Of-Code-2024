from lock_key_matcher import LockKeyMatcher
from schematic import Schematic


def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read()

    schematics = [
        [[value for value in line] for line in schematic.splitlines()] 
        for schematic in content.split('\n\n')
    ]

    locks = [Schematic(schematic) for schematic in schematics if Schematic(schematic).is_lock()]
    keys = [Schematic(schematic) for schematic in schematics if not Schematic(schematic).is_lock()]

    matcher = LockKeyMatcher(locks, keys)
    unique_lock_key_pairs = matcher.get_unique_lock_key_pairs()
    print(f'Total lock/key pairs: {len(unique_lock_key_pairs)}')


if __name__ == '__main__':
    main()
