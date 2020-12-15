import re
import itertools


def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    instructions = []
    for line in lines:
        key, value = line.strip().split("=")
        instructions.append([key.strip(), value.strip()])
    return instructions


instructions = read_input()

# part 1
mask = ""
memory_bitmap = {}
for instruction in instructions:
    if instruction[0] == "mask":
        mask = list(instruction[1])
    else:
        mem_address = re.findall(r"\d+", instruction[0])[0]
        bin_value = "{0:b}".format(int(instruction[1]))
        bin_value = list("0" * (len(mask) - len(bin_value)) + bin_value)
        for idx, bit in enumerate(list(mask)):
            if bit != "X":
                bin_value[idx] = bit
        bin_value = "".join(bin_value)
        memory_bitmap[mem_address] = int(bin_value, 2)

mem_values_sum = 0
for value in memory_bitmap.values():
    mem_values_sum += value

print(mem_values_sum)


# part 2
mask = ""
results = []
floating_memory_bitmap = {}
for instruction in instructions:
    if instruction[0] == "mask":
        mask = list(instruction[1])
    else:
        mem_address = re.findall(r"\d+", instruction[0])[0]
        bin_value = "{0:b}".format(int(mem_address))
        bin_value = list("0" * (len(mask) - len(bin_value)) + bin_value)
        for idx, bit in enumerate(list(bin_value)):
            if mask[idx] in ["X", "1"]:
                bin_value[idx] = mask[idx]
        floating_memory_bitmap["".join(bin_value)] = int(instruction[1])

memory_bitmap = {}
for mem_address, value in floating_memory_bitmap.items():
    combinations = [list(mem_address)]
    while "X" in list(itertools.chain.from_iterable(combinations)):
        for idx_c, combination in enumerate(combinations):
            for idx, bit in enumerate(list(combination)):
                if bit == "X":
                    ver_0, ver_1 = list(combination), list(combination)
                    ver_0[idx], ver_1[idx] = "0", "1"
                    del combinations[idx_c]
                    combinations.extend([ver_0, ver_1])
                    break
    decimal_results = []
    for combination in combinations:
        str_bitmap = "".join(combination)
        memory_bitmap[str_bitmap] = value

result = 0
for value in memory_bitmap.values():
    result += value

print(result)
