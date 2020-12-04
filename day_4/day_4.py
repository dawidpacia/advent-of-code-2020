import re


def read_input():
    passports = []
    with open("input.txt") as report_data:
        lines = report_data.readlines()

    pass_elements = []
    passport = {}
    for line in lines:
        if line.strip():
            pass_elements.extend(line.split())
        else:
            for element in pass_elements:
                key, value = element.split(":")
                passport[key] = value
            passports.append(passport)
            pass_elements = []
            passport = {}
    return passports


def byr(year):
    if 1920 <= int(year) <= 2002:
        return True
    return False


def iyr(year):
    if 2010 <= int(year) <= 2020:
        return True
    return False


def eyr(year):
    if 2020 <= int(year) <= 2030:
        return True
    return False


def hgt(height):
    if height[-2:] == "cm" and 150 <= int(height[:-2]) <= 193:
        return True
    if height[-2:] == "in" and 59 <= int(height[:-2]) <= 76:
        return True
    return False


def hcl(colour):
    if re.search("^#[a-f0-9]{6}$", colour):
        return True
    return False


def ecl(colour):
    if colour in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False


def pid(number):
    if re.search("^[0-9]{9}$", number) and len(number) == 9:
        return True
    return False


mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]


def check_if_valid_passport(passport_data):
    for field in mandatory_fields:
        if field not in passport_data:
            return False
    return True


passports = read_input()

# Part 1
valid_passports = 0
for passport in passports:
    valid_passports += check_if_valid_passport(passport)

print(valid_passports)

# Part 2
valid_passports_2 = 0
for passport in passports:
    if "cid" in passport:
        del passport["cid"]
    if check_if_valid_passport(passport):
        valid = True
        for key, value in passport.items():
            if not locals()[key](value):
                valid = False
                break
        valid_passports_2 += valid

print(valid_passports_2)
