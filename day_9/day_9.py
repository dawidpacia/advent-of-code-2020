def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    numbers_list = [int(number) for number in lines]

    return numbers_list


numbers = read_input()


def check_if_valid(numbers):
    number_to_check = numbers[-1]
    for value_1 in numbers[:-1]:
        for value_2 in numbers[:-2]:
            if value_1 + value_2 == number_to_check:
                return True
    return False


# part 1
preamble, invalid_number_idx, invalid_number = 25, 0, 0
for idx, number in enumerate(numbers[preamble:]):
    if not check_if_valid(numbers[idx : preamble + idx + 1]):
        invalid_number, invalid_number_idx = number, idx
        print(invalid_number)


# part 2
for idx_start in range(invalid_number_idx):
    for idx_finish in range(idx_start + 2, invalid_number_idx):
        if sum(numbers[idx_start:idx_finish]) == invalid_number:
            print(min(numbers[idx_start:idx_finish]) + max(numbers[idx_start:idx_finish]))
