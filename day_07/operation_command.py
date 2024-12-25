from abc import ABC, abstractmethod


class OperationCommand(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        raise NotImplementedError()

class AddCommand(OperationCommand):
    def execute(self, a: int, b: int) -> int:
        return a + b

class MultiplyCommand(OperationCommand):
    def execute(self, a: int, b: int) -> int:
        return a * b

class ConcatenateCommand(OperationCommand):
    def execute(self, a: int, b: int) -> int:
        multiplier = 10
        
        while multiplier <= b:
            multiplier *= 10
        
        return (a * multiplier) + b
