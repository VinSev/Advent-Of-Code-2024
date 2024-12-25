from instruction_parser import InstructionParser


class MemoryProcessor:
    def __init__(self, memory: str, instruction_parser: 'InstructionParser') -> None:
        self._memory = memory
        self._instruction_parser = instruction_parser

    def process_instructions(self) -> int:
        instructions = self._instruction_parser.parse_memory(self._memory)
        handler = self._instruction_parser.get_instruction_handler()
        
        return sum(handler.handle_instruction(instruction) for instruction in instructions)
