import multiprocessing
from typing import List, Tuple

from equation_processor import EquationProcessor


class CalibrationCalculator():
    def __init__(self, equations: List[Tuple[int, List[int]]], operations: List[str]):
        self._equations = equations
        self._operations = operations
        self._equation_processor = EquationProcessor()
    
    def calculate_total_result(self) -> int:
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as thread_pool:
            equation_parameters = [(target, numbers, self._operations) for target, numbers in self._equations]
            calibration_results = thread_pool.starmap(self._equation_processor.process_equation, equation_parameters)
            
            return sum(calibration_results)
