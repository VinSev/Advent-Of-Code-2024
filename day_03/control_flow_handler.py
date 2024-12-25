from abc import abstractmethod

from instruction_handler import InstructionHandler


class ControlFlowHandler(InstructionHandler): 
    @abstractmethod
    def is_enabled(self) -> bool:
        raise NotImplementedError
    

class DoDontHandler(ControlFlowHandler):
    def __init__(self) -> None:
        self._enabled = True

    def handle_instruction(self, instruction: str) -> int:
        actions = {
            'do()': self._enable,
            'don\'t()': self._disable
        }
        
        return actions.get(instruction, self._no_action)()

    def is_enabled(self) -> bool:
        return self._enabled
    
    def _enable(self) -> int:
        self._enabled = True
        
        return 1
    
    def _disable(self) -> int:
        self._enabled = False
        
        return 1
    
    def _no_action(self) -> int:
        return 0
