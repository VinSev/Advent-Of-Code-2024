from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from instruction_regex_util import InstructionRegexUtil

if TYPE_CHECKING:
    from control_flow_handler import ControlFlowHandler


class InstructionHandler(ABC):
    @abstractmethod
    def handle_instruction(self, instruction: str) -> int:
        raise NotImplementedError


class MultiplicationHandler(InstructionHandler):
    def handle_instruction(self, instruction: str) -> int:
        a, b = InstructionRegexUtil.find_all_digits(instruction)
        
        return a * b

        
class AdaptiveHandler(InstructionHandler):
    def __init__(
        self, 
        control_flow_handler: 'ControlFlowHandler', 
        instruction_handler: 'InstructionHandler'
    ) -> None:
        self._control_flow_handler = control_flow_handler
        self._instruction_handler = instruction_handler

    def handle_instruction(self, instruction: str) -> int:     
        if InstructionRegexUtil.match_multiplication(instruction):
            if self._control_flow_handler.is_enabled():
                return self._instruction_handler.handle_instruction(instruction)
            
            return 0
        
        self._control_flow_handler.handle_instruction(instruction)
        
        return 0
