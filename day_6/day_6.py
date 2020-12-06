def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()

    group, groups, = [], []
    for line in lines:
        if not line.strip():
            groups.append(group)
            group = []
        else:
            group.append(line.strip())

    return groups


groups = read_input()
answers = ""
list_of_answers = []

# part 1
for group in groups:
    answers = ""
    for person in group:
        answers += person
    list_of_answers.append(answers)

sum_of_counts = 0
for answer in list_of_answers:
    sum_of_counts += len(set(answer))

print(sum_of_counts)

# part 2
sum_of_counts = 0
for group in groups:
    group_set, valid = set(group[0]), True
    for person in group:
        group_set = set(group_set.intersection(person))
    sum_of_counts += len(group_set)

print(sum_of_counts)
