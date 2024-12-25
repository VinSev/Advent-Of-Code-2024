from file_reader import FileReader
from instruction_parser import (AdaptiveInstructionParser, 
                                SimpleInstructionParser)
from memory_processor import MemoryProcessor


def main() -> None:
    corrupted_memory = FileReader.read_file('data.txt')

    instruction_parser = SimpleInstructionParser()
    memory_processor = MemoryProcessor(corrupted_memory, instruction_parser)
    simple_result = memory_processor.process_instructions()
    print(f'Simple Instructions Result: {simple_result}')

    instruction_parser = AdaptiveInstructionParser()
    memory_processor = MemoryProcessor(corrupted_memory, instruction_parser)
    adaptive_result = memory_processor.process_instructions()
    print(f'Adaptive Instructions Result: {adaptive_result}')


if __name__ == '__main__':
    main()
