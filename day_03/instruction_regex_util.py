import re
from typing import List


class InstructionRegexUtil():
    MULTIPLICATION_PATTERN = r'mul\(\d+,\d+\)'
    DO_PATTERN = r'do\(\)'
    DONT_PATTERN = r'don\'t\(\)'
    DIGIT_PATTERN = r'\d+'

    @staticmethod
    def match_multiplication(instruction: str) -> bool:
        return bool(re.fullmatch(InstructionRegexUtil.MULTIPLICATION_PATTERN, instruction))

    @staticmethod
    def find_all_digits(instruction: str) -> List[int]:
        return list(map(int, re.findall(InstructionRegexUtil.DIGIT_PATTERN, instruction)))

    @staticmethod
    def parse_simple_memory(memory: str) -> List[str]:
        return re.findall(InstructionRegexUtil.MULTIPLICATION_PATTERN, memory)
    
    @staticmethod
    def parse_adaptive_memory(memory: str) -> List[str]:
        pattern = f'{InstructionRegexUtil.MULTIPLICATION_PATTERN}|{InstructionRegexUtil.DO_PATTERN}|{InstructionRegexUtil.DONT_PATTERN}'
        
        return re.findall(pattern, memory)
