from abc import ABC, abstractmethod
from typing import List


class ReportSafetyStrategy(ABC):
    @abstractmethod
    def is_safe(self, report: List[int]) -> bool:
        raise NotImplementedError
    
    def _is_safe_report(self, report: List[int]) -> bool:
        if self._is_valid_difference(report):
            return self._is_increasing(report) or self._is_decreasing(report)
        
        return False
    
    def _is_valid_difference(self, report: List[int]) -> bool:
        for i in range(len(report) - 1):
            difference = abs(report[i] - report[i + 1])
            
            if not (1 <= difference <= 3):
                return False
            
        return True

    def _is_increasing(self, report: List[int]) -> bool:
        for i in range(len(report) - 1):
            if not (report[i] <= report[i + 1]):
                return False
            
        return True

    def _is_decreasing(self, report: List[int]) -> bool:
        for i in range(len(report) - 1):
            if not (report[i] >= report[i + 1]):
                return False
            
        return True


class StrictReportSafetyStrategy(ReportSafetyStrategy):
    def is_safe(self, report: List[int]) -> bool:
        return self._is_safe_report(report)
 
    
class SingleRemovalReportSafetyStrategy(ReportSafetyStrategy):
    def is_safe(self, report: List[int]) -> bool:
        if self._is_safe_report(report):
            return True
        
        return self._is_report_safe_with_single_removal(report)
    
    def _is_report_safe_with_single_removal(self, report: List[int]) -> bool:
        for i in range(len(report)):
            partial_report = report[:i] + report[i + 1:]
            
            if self._is_safe_report(partial_report):
                return True
            
        return False
