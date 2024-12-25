from typing import List

from report_safety_strategy import ReportSafetyStrategy


class ReportAnalyzer():
    def __init__(self, reports: List[List[int]], safety_strategy: ReportSafetyStrategy) -> None:
        self._reports = reports
        self._safety_strategy = safety_strategy

    def count_safe_reports(self) -> int:
        safe_report_count = 0
        
        for report in self._reports:
            if self._safety_strategy.is_safe(report):
                safe_report_count += 1
        
        return safe_report_count
    