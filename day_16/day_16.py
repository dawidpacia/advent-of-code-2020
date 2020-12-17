def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    valid_fields_range = {}
    idx = 0
    while lines[idx] != "\n":
        field, values = lines[idx].split(":")
        ranges = values.strip().split("or")
        val_range = [[int(val) for val in rang.split("-")] for rang in ranges]
        valid_fields_range[field] = val_range
        idx += 1
    your_ticket = [int(number) for number in lines[idx + 2].split(",")]
    nearby_tickets = []
    for line in lines[idx + 5 :]:
        nearby_tickets.append([int(number) for number in line.split(",")])
    return valid_fields_range, your_ticket, nearby_tickets


def check_ticket_value(valid_fields_range: dict, ticket_value):
    for range_values in valid_fields_range.values():
        range_1, range_2 = range_values
        if range_1[0] <= ticket_value <= range_1[1] or range_2[0] <= ticket_value <= range_2[1]:
            return True
    return False


valid_fields_range, your_ticket, nearby_tickets = read_input()

# part 1
scanning_error_rate = 0
valid_tickets = []
for ticket in nearby_tickets:
    is_valid = True
    for ticket_value in ticket:
        if not check_ticket_value(valid_fields_range, ticket_value):
            scanning_error_rate += ticket_value
            is_valid = False
    if is_valid:
        valid_tickets.append(ticket)
print(scanning_error_rate)


def check_if_field_possible(ranges, ticket_value):
    if ranges[0][0] <= ticket_value <= ranges[0][1] or ranges[1][0] <= ticket_value <= ranges[1][1]:
        return True
    return False


# part 2
possible_fields = []
for i in range(len(valid_tickets[0])):
    applicable_fields = []
    for field, ranges in valid_fields_range.items():
        is_field_correct = True
        for ticket in valid_tickets:
            if not check_if_field_possible(ranges, ticket[i]):
                is_field_correct = False
                break
        if is_field_correct:
            applicable_fields.append(field)
    possible_fields.append(applicable_fields)

found_fields_idx = {}
for i in range(len(valid_fields_range)):
    for field_idx, fields in enumerate(possible_fields):
        if len(fields) == i + 1:
            for field in fields:
                if field not in found_fields_idx:
                    found_fields_idx[field] = field_idx

result = 1
for field, idx in found_fields_idx.items():
    if "departure" in field:
        result *= your_ticket[idx]
        print(result, field, idx)

print(result)
