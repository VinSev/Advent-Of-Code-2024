from file_reader import FileReader
from report_safety_strategy import StrictReportSafetyStrategy, SingleRemovalReportSafetyStrategy
from report_analyzer import ReportAnalyzer


def main() -> None:
    reports = FileReader.read_matrix('data.txt', target_type=int, separator=' ')

    safety_strategy = StrictReportSafetyStrategy()
    report_analyzer = ReportAnalyzer(reports, safety_strategy)
    
    strictly_safe_report_count = report_analyzer.count_safe_reports()
    print(f'Strictly Safe Reports: {strictly_safe_report_count}')
    
    safety_strategy = SingleRemovalReportSafetyStrategy()
    report_analyzer = ReportAnalyzer(reports, safety_strategy)
    
    single_removal_safe_report_count = report_analyzer.count_safe_reports()
    print(f'Single Removal Safe Reports: {single_removal_safe_report_count}')


if __name__ == '__main__':
    main()
