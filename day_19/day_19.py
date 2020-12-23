import itertools
import re
import time

start_time = time.time()


def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    rules = {}
    messages = []
    for rule in lines:
        if ":" in rule:
            key, value = rule.strip().split(":")
            subrules = value.strip().split("|")
            for subrule in subrules:
                try:
                    rules[key].append(subrule.strip().split())
                except KeyError:
                    rules[key] = [subrule.strip().replace('"', "").split()]
        elif rule != "\n":
            messages.append(rule.strip())

    return rules, messages


def check_if_fits_any_message(rules, messages):
    sub_string = [char for char in rules if not char.isdigit()]
    for message in messages:
        if "".join(sub_string) == message[: len(sub_string)]:
            return True
    return False


def check_if_not_duplicate(new_rule, combinations):
    if new_rule in combinations:
        return False
    return True


rules, messages = read_input()
print(rules)

combinations = rules["0"]
char_chain = list(itertools.chain.from_iterable(rules))
max_message_len = max([len(message) for message in messages])

while char_chain.count("a") + char_chain.count("b") != len(char_chain):
    for i_global, combination in enumerate(combinations):
        if re.findall("\d", "".join(combination)):
            for i, rule in enumerate(combination):
                if rule.isdigit():
                    del combinations[i_global]
                    for subrule in rules[rule]:
                        skip = False
                        new_rules = list(combination)
                        new_rules[i : i + 1] = subrule
                        if not check_if_not_duplicate(new_rules, combinations) or len(new_rules) > max_message_len:
                            combinations.remove(new_rules)
                            skip = True
                        if check_if_fits_any_message(new_rules, messages) and not skip:
                            combinations.append(new_rules)
                    break

    char_chain = list(itertools.chain.from_iterable(combinations))

char_combinations = []
for combination in combinations:
    char_combinations.append("".join(combination))

result = 0
for message in messages:
    if message in char_combinations:
        result += 1

print(result)
print(time.time() - start_time)
