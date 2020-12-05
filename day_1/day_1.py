def read_input():
    expenses = []

    with open("input.txt") as report_data:
        lines = report_data.readlines()

    for line in lines:
        expenses.append(int(line))

    return expenses


def calculate_result(expenses):
    while len(expenses) != 1:
        first_value = expenses[0]
        for value in expenses:
            if first_value + value == 2020:
                result = first_value * value
                return result
        del expenses[0]


expenses = read_input()
print(calculate_result(expenses))

# part 2


def calculate_result_3(expenses):
    while len(expenses) != 0:
        value_1 = expenses[0]
        for value_2 in expenses[1:]:
            for value_3 in expenses[2:]:
                if value_1 + value_2 + value_3 == 2020:
                    result = value_1 * value_2 * value_3
                    return result
        del expenses[0]
    print(expenses)


expenses = read_input()
print(calculate_result_3(expenses))
