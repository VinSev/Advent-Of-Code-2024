import itertools
from typing import List

from operation_command import AddCommand, MultiplyCommand, ConcatenateCommand


class EquationProcessor():
    def __init__(self):
        self._commands = {
            '+': AddCommand(),
            '*': MultiplyCommand(),
            '||': ConcatenateCommand()
        }
    
    def _apply_operation(self, a: int, b: int, operation: str) -> int:
        command = self._commands.get(operation)
        
        if command is None:
            raise ValueError(f'Operation ({operation}) Not Found.')
        
        return command.execute(a, b)

    def _evaluate_expression(self, target: int, numbers: List[int], operations: List[str]) -> bool:
        result = numbers[0]
        
        for number, operation in zip(numbers[1:], operations):
            result = self._apply_operation(result, number, operation)
            
            if result > target:
                return False
        
        return result == target

    def _is_solvable(self, target: int, numbers: List[int], operations: List[str]) -> bool:
        number_of_operations = len(numbers) - 1

        for operation_combination in itertools.product(operations, repeat=number_of_operations):
            if self._evaluate_expression(target, numbers, operation_combination):
                return True
        
        return False

    def process_equation(self, target: int, numbers: List[int], operations: List[str]) -> int:
        return target if self._is_solvable(target, numbers, operations) else 0
