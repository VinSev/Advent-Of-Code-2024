from memory_processor import MemoryProcessor
from memory_type import MemoryType
from point import Point

BIT = 1
BYTE = 8 * BIT
KILOBYTE = 128 * BYTE


def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read()
        
    falling_bytes = [tuple(int(value) for value in line.split(',')) for line in content.splitlines()]

    size = 71
    memory = [[MemoryType.SAFE for _ in range(size)] for _ in range(size)]

    start = Point(0, 0)
    exit = Point(size - 1, size - 1)
    
    memory_processor = MemoryProcessor(memory, falling_bytes, start, exit)

    memory_processor.corrupt_memory(byte_amount=KILOBYTE)
    steps_to_exit = memory_processor.min_steps_to_exit()
    print(f'Minimal steps to exit: {steps_to_exit}')
    
    blocking_byte = memory_processor.first_blocking_byte()
    print(f'First byte that blocks the exit: {blocking_byte}')
    
if __name__ == '__main__':
    main()
