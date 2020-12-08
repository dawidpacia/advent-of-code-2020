def read_input():
    program = []
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    for line in lines:
        instr, value = line.split()
        program.append((instr, int(value)))

    return program


program = read_input()


# part 1
list_of_idxs = []
idx, accumulator = 0, 0

while idx not in list_of_idxs:
    list_of_idxs.append(idx)
    if program[idx][0] == "nop":
        idx += 1
    elif program[idx][0] == "acc":
        accumulator += program[idx][1]
        idx += 1
    elif program[idx][0] == "jmp":
        idx += program[idx][1]

print(accumulator)


# part 2
changed_instructions_idxs = []

idx = 0
while idx != len(program):
    used_idxs, idx, accumulator = [], 0, 0
    instr_changed = False
    while idx not in used_idxs and idx != len(program):
        instr, value = program[idx][0], program[idx][1]
        used_idxs.append(idx)
        if instr == "jmp" and not instr_changed and idx not in changed_instructions_idxs:
            changed_instructions_idxs.append(idx)
            instr_changed = True
            idx += 1
        elif instr == "nop" and not instr_changed and idx not in changed_instructions_idxs:
            changed_instructions_idxs.append(idx)
            instr_changed = True
            idx += value
        elif instr == "nop":
            idx += 1
        elif instr == "jmp":
            idx += program[idx][1]
        elif instr == "acc":
            accumulator += value
            idx += 1

print(accumulator)
