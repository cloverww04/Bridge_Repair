import itertools

def find_valid_expressions(total, numbers):
    operators = ['+', '*']
    operator_combinations = itertools.product(operators, repeat=len(numbers) - 1)

    valid_expressions = []

    for op_combo in operator_combinations:
        expression = str(numbers[0])
        for i in range(1, len(numbers)):
            expression = f"({expression} {op_combo[i-1]} {numbers[i]})"

        if eval(expression) == total:
            valid_expressions.append(expression)

    return valid_expressions


thisdict = {}

with open('data1.txt', 'r') as file:
    for line in file:
        parts = line.split(':')
        total = int(parts[0].strip())
        values = list(map(int, parts[1].strip().split()))
        thisdict[total] = values

calibration_result = 0

for total, numbers in thisdict.items():
    valid_expressions = find_valid_expressions(total, numbers)
    if valid_expressions:
        print(f"Valid expressions for {total}:")
        for expression in valid_expressions:
            print(f"  {expression}")
        
        calibration_result += total
    else:
        print(f"No valid expressions for {total}")

print(f"\nTotal Calibration Result: {calibration_result}")
