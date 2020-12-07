def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    bags_map = {}
    for line in lines:
        key, value = line.split("contain")
        bag_key = " ".join(key.split()[:2])
        bags_map[bag_key] = {}
        bags_value = value.split(",")
        for bag in bags_value:
            if "no other" in bag:
                bags_map[bag_key] = 0
            else:
                amount, inter_bag_key = bag.split()[0], " ".join(bag.split()[1:3])
                bags_map[bag_key][inter_bag_key] = int(amount)
    return bags_map


bags_map = read_input()


def find_shiny_gold(bag):
    if bags_map[bag]:
        for inter_bag in bags_map[bag]:
            if inter_bag == "shiny gold":
                return True
            if find_shiny_gold(inter_bag):
                return True
    return False


def find_total_bags(bag_colour, num_of_bags):
    total_bags = num_of_bags
    if bags_map[bag_colour]:
        for inter_bag in bags_map[bag_colour]:
            total_bags += find_total_bags(inter_bag, num_of_bags * bags_map[bag_colour][inter_bag])
        return total_bags
    return num_of_bags


# part 1
bags_found = 0
for bag in bags_map:
    bags_found += find_shiny_gold(bag)

print(bags_found)

# part 2
total_bags = find_total_bags("shiny gold", 1) - 1

print(total_bags)
