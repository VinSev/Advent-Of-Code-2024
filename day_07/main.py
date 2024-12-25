from calibration_calculator import CalibrationCalculator


def main() -> None:
    with open('data.txt', 'r') as file:
        content = file.read()
    
    equations = []

    for line in content.splitlines():
        target, values = line.split(':')
        equation = (int(target), tuple(int(value) for value in values.split()))
        equations.append(equation)
    
    operations = ['+', '*']
    calibration_calculator = CalibrationCalculator(equations, operations)
    total_calibration_result = calibration_calculator.calculate_total_result()
    print(f'Total Calibration Result with Operations {operations}: {total_calibration_result}')
    
    operations = ['+', '*', '||']
    calibration_calculator = CalibrationCalculator(equations, operations)
    total_calibration_result = calibration_calculator.calculate_total_result()
    print(f'Total Calibration Result with Operations {operations}: {total_calibration_result}')


if __name__ == '__main__':
    main()
