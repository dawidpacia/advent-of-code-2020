from time import time


def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    seats_map = [list(seats_row.strip()) for seats_row in lines]

    return seats_map


current_map = read_input()
map_size = (len(current_map[0]), len(current_map))


def get_vectors(x, y):
    if x == 0:
        x_vector = [0, 1]
    elif x == map_size[0] - 1:
        x_vector = [-1, 0]
    else:
        x_vector = [-1, 0, 1]

    if y == 0:
        y_vector = [0, 1]
    elif y == map_size[1] - 1:
        y_vector = [-1, 0]
    else:
        y_vector = [-1, 0, 1]

    return x_vector, y_vector


def get_new_seat(current_map, x, y):
    place_symbol = current_map[y][x]
    if place_symbol == ".":
        return "."
    x_vector, y_vector = get_vectors(x, y)

    adjacent_occupied = 0
    for x_step in x_vector:
        for y_step in y_vector:
            x_pointer, y_pointer = x + x_step, y + y_step
            if place_symbol == "L" and current_map[y_pointer][x_pointer] == "#":
                return "L"
            if place_symbol == "#" and current_map[y_pointer][x_pointer] == "#":
                adjacent_occupied += 1
                if adjacent_occupied >= 5:
                    return "L"
    return "#"


def check_if_occupied_visible(x_pos, y_pos, x_vector, y_vector, seats_map):
    try:
        while True:
            x_pos += x_vector
            y_pos += y_vector
            if x_pos < 0 or y_pos < 0:
                return False
            if seats_map[y_pos][x_pos] == "#":
                return True
            if seats_map[y_pos][x_pos] == "L":
                return False
    except IndexError:
        return False


def get_new_seat_fix(current_map, x, y):
    place_symbol = current_map[y][x]
    if place_symbol == ".":
        return "."
    x_vector, y_vector = get_vectors(x, y)

    visible_occupied = 0
    for x_step in x_vector:
        for y_step in y_vector:
            if not x_step and not y_step:
                continue
            if place_symbol == "L" and check_if_occupied_visible(x, y, x_step, y_step, current_map):
                return "L"
            if place_symbol == "#" and check_if_occupied_visible(x, y, x_step, y_step, current_map):
                visible_occupied += 1
                if visible_occupied >= 5:
                    return "L"
    return "#"


start_time = time()

new_map = [["" for x in range(map_size[0])] for y in range(map_size[1])]


counter = 0
while True:
    counter += 1
    for x in range(map_size[0]):
        for y in range(map_size[1]):
            symbol = get_new_seat(current_map, x, y)
            new_map[y][x] = symbol
    if current_map == new_map:
        break
    current_map = [row[:] for row in new_map]


num_of_occupied_seats = 0
for x in range(map_size[0]):
    for y in range(map_size[1]):
        if current_map[y][x] == "#":
            num_of_occupied_seats += 1

print("part 1 time {}".format(time() - start_time))
print("num of seating iterations: {}".format(counter))
print("num of seats occupied: {}\n".format(num_of_occupied_seats))


# part 2
start_time = time()
current_map = read_input()
counter = 0
while True:
    counter += 1
    for x in range(map_size[0]):
        for y in range(map_size[1]):
            symbol = get_new_seat_fix(current_map, x, y)
            new_map[y][x] = symbol
    if current_map == new_map:
        break
    current_map = [row[:] for row in new_map]

num_of_occupied_seats = 0
for x in range(map_size[0]):
    for y in range(map_size[1]):
        if current_map[y][x] == "#":
            num_of_occupied_seats += 1
print("part 2 time {}".format(time() - start_time))
print("num of seating iterations: {}".format(counter))
print("num of seats occupied: {}".format(num_of_occupied_seats))
