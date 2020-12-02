
def read_input():
    passwords_policy = []

    with open("input.txt") as report_data:
        lines = report_data.readlines()

    for line in lines:
        values_range, letter, password = line.split()
        min_value, max_value = values_range.split("-")
        letter = letter[0]
        passwd_policy = {
            "min": int(min_value),
            "max": int(max_value),
            "letter": letter,
            "password": password
        }
        passwords_policy.append(passwd_policy)
    return passwords_policy


passwords_policy = read_input()

# part 1
num_of_valid_passwords = 0
for password_policy in passwords_policy:
    occurrences = password_policy["password"].count(password_policy["letter"])
    if password_policy["min"] <= occurrences <= password_policy["max"]:
        num_of_valid_passwords += 1

print(num_of_valid_passwords)

# part 2
num_of_valid_passwords = 0
for password_policy in passwords_policy:
    password, first_idx, second_idx, letter = \
        password_policy["password"], password_policy["min"], password_policy["max"], password_policy["letter"]
    if bool(password[first_idx-1] == letter) != bool(password[second_idx-1] == letter):
        num_of_valid_passwords += 1

print(num_of_valid_passwords)
