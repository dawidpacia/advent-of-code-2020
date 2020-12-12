import math


def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    commands = [[command.strip()[0], int(command.strip()[1:])] for command in lines]
    return commands


commands = read_input()
current_angle = 0
current_pos = [0, 0]

direction_vectors = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}


def calibrate_angle(angle, command):
    if command[0] == "L":
        angle -= command[1]
    elif command[0] == "R":
        angle += command[1]

    if angle < 0:
        angle += 360
    elif angle >= 360:
        angle -= 360

    return angle


def rotate_waypoint(current_pos, waypoint_pos, command):
    x_cur, y_cur = current_pos
    x_way, y_way = x_cur + waypoint_pos[0], y_cur + waypoint_pos[1]

    if command[0] == "R":
        radians = math.radians(command[1])
    if command[0] == "L":
        radians = math.radians(command[1]) * -1

    x_way_fin = x_cur + math.cos(radians) * (x_way - x_cur) + math.sin(radians) * (y_way - y_cur)
    y_way_fin = y_cur + -math.sin(radians) * (x_way - x_cur) + math.cos(radians) * (y_way - y_cur)

    return [int(x_way_fin - x_cur), int(y_way_fin - y_cur)]


def move_forward(angle, value):
    if angle % 360 == 0:
        return make_nsew_move(["E", value])
    if angle % 360 == 90:
        return make_nsew_move(["S", value])
    if angle % 360 == 180:
        return make_nsew_move(["W", value])
    if angle % 360 == 270:
        return make_nsew_move(["N", value])


def make_nsew_move(command):
    unit_vector = direction_vectors[command[0]]
    move_vector = [value * command[1] for value in unit_vector]
    return move_vector


def move_ship_to_waypoint(current_pos, waypoint_pos, value):
    x_pos = current_pos[0] + value * waypoint_pos[0]
    y_pos = current_pos[1] + value * waypoint_pos[1]
    return [x_pos, y_pos]


# part 1
for command in commands:
    move_vector = [0, 0]
    if command[0] in ["N", "S", "E", "W"]:
        move_vector = make_nsew_move(command)
    elif command[0] in ["L", "R"]:
        current_angle = calibrate_angle(current_angle, command)
    elif command[0] == "F":
        move_vector = move_forward(current_angle, command[1])

    for i in range(2):
        current_pos[i] += move_vector[i]

print(abs(current_pos[0]) + abs(current_pos[1]))


# part 2
current_pos = [0, 0]
waypoint_pos = [10, 1]
for command in commands:
    if command[0] in ["N", "S", "E", "W"]:
        move_vector = make_nsew_move(command)
        for i in range(2):
            waypoint_pos[i] += move_vector[i]
    elif command[0] in ["L", "R"]:
        waypoint_pos = rotate_waypoint(current_pos, waypoint_pos, command)
    elif command[0] == "F":
        current_pos = move_ship_to_waypoint(current_pos, waypoint_pos, command[1])

print(abs(current_pos[0]) + abs(current_pos[1]))
