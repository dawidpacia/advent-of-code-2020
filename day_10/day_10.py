def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    numbers_list = sorted([int(number) for number in lines])

    return numbers_list


adapters_sorted = read_input()

device_joltage = max(adapters_sorted) + 3

adapters_sorted.insert(0, 0)  # outlet
adapters_sorted.append(device_joltage)

# part 1
diff_1_joltage, diff_3_joltage = 0, 0
for idx, adapter_value in enumerate(adapters_sorted[:-1]):
    diff = adapters_sorted[idx + 1] - adapter_value
    if diff == 1:
        diff_1_joltage += 1
    elif diff == 3:
        diff_3_joltage += 1
    else:
        raise ValueError

print(diff_1_joltage * diff_3_joltage)

# part 2
subsequence_combinations = {1: 1, 2: 1, 3: 2, 4: 4, 5: 7}

num_of_following_sequence = 1
result = 1

for idx, adapter_value in enumerate(adapters_sorted[:-1]):
    if adapters_sorted[idx + 1] - adapter_value == 1:
        num_of_following_sequence += 1
    else:
        result *= subsequence_combinations[num_of_following_sequence]
        num_of_following_sequence = 1

print(result)
