import time


def read_input():
    with open("input.txt") as report_data:
        line = report_data.readlines()
    numbers = line[0].split(",")
    numbers_turns = {}
    for idx, value in enumerate(numbers[:-1]):
        numbers_turns[value] = idx + 1
    last_number = numbers[-1]
    return numbers_turns, last_number


def get_nth_answer(num_of_last_answer):
    numbers_turns_dict, last_number = read_input()
    idx = len(numbers_turns_dict) + 1
    for i in range(idx, num_of_last_answer):
        if str(last_number) not in numbers_turns_dict.keys():
            numbers_turns_dict[str(last_number)] = i
            last_number = 0
        else:
            diff = i - numbers_turns_dict[str(last_number)]
            numbers_turns_dict[str(last_number)] = i
            last_number = diff
        if i % 1000000 == 0:
            print(i)
    return last_number


start_time = time.time()
print(get_nth_answer(2020))
print(get_nth_answer(30000000))
print("Time taken: {}".format(time.time() - start_time))
