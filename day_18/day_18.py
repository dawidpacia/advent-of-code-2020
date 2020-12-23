def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    operations = []
    for line in lines:
        operation = [line[0]]
        for idx, char in enumerate(line.strip()[1:]):
            if char != " ":
                if char in "0123456789" and line[idx] in "0123456789":
                    operation[-1] += char
                else:
                    operation.append(char)
        operations.append(operation)
    return operations


def make_operation(value_1, operator, value_2):
    if operator == "*":
        return int(value_1) * int(value_2)
    if operator == "+":
        return int(value_1) + int(value_2)
    return False


operations = read_input()
results = 0

for operation in operations:
    operation.reverse()
    while "(" in operation:
        new_operation = []
        for idx in range(len(operation) - 3):
            if operation[idx + 3] == "(":
                result = str(make_operation(*operation[idx : idx + 3]))
                if operation[idx - 1] == ")":
                    new_operation[-1] = result
                else:
                    new_operation.extend([result, "("])
                new_operation.extend(operation[idx + 4 :])
                break
            new_operation.append(operation[idx])
        operation = list(new_operation)
    operation.reverse()
    while len(operation) > 1:
        new_operation = [str(make_operation(*operation[:3]))]
        new_operation.extend(operation[3:])
        operation = list(new_operation)
    results += int(operation[0])

print(results)

# part 2
def calculate_subexpresion(expression):
    while "+" in expression:
        for i, char in enumerate(expression):
            if char == "+":
                new_operation = expression[: i - 1]
                operation_result = str(make_operation(*expression[i - 1 : i + 2]))
                new_operation.append(operation_result)
                new_operation.extend(expression[i + 2 :])
                expression = list(new_operation)
                break

    while len(expression) > 1:
        new_operation = [str(make_operation(*expression[:3]))]
        new_operation.extend(expression[3:])
        expression = list(new_operation)
    return int(expression[0])


operations = read_input()
result = 0
for operation in operations:
    left_bracket_idx = 0
    while "(" in operation:
        new_operation = []
        for i, char in enumerate(operation):
            if char == "(":
                left_bracket_idx = i
            if char == ")":
                new_operation = operation[:left_bracket_idx]
                expression_result = str(calculate_subexpresion(operation[left_bracket_idx + 1 : i]))
                new_operation.append(expression_result)
                new_operation.extend(operation[i + 1 :])
                operation = list(new_operation)
                break
        operation = list(new_operation)
    result += int(calculate_subexpresion(operation))
print(result)
