from abc import ABC, abstractmethod
from typing import List

from control_flow_handler import DoDontHandler
from instruction_regex_util import InstructionRegexUtil
from instruction_handler import (AdaptiveHandler, 
                                 InstructionHandler,
                                 MultiplicationHandler)


class InstructionParser(ABC):
    @abstractmethod
    def parse_memory(self, memory: str) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def get_instruction_handler(self) -> 'InstructionHandler':
        raise NotImplementedError


class SimpleInstructionParser(InstructionParser):
    def parse_memory(self, memory: str) -> List[str]:
        return InstructionRegexUtil.parse_simple_memory(memory)

    def get_instruction_handler(self) -> 'InstructionHandler':
        return MultiplicationHandler()


class AdaptiveInstructionParser(InstructionParser):
    def parse_memory(self, memory: str) -> List[str]:
        return InstructionRegexUtil.parse_adaptive_memory(memory)
    
    def get_instruction_handler(self) -> 'InstructionHandler':
        control_flow_handler = DoDontHandler()
        instruction_handler = MultiplicationHandler()
        
        return AdaptiveHandler(control_flow_handler, instruction_handler)
