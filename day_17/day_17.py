import itertools
import copy


def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    cube_layer = [[element for element in line.strip()] for line in lines]
    return cube_layer


cycles = 6
initial_layer = read_input()
xy_size = cycles * 2 + len(initial_layer)
z_size = cycles * 2 + 1

# order - z, y, x
cube = [[["." for _ in range(xy_size)] for _ in range(xy_size)] for _ in range(z_size)]
new_cube = [[["." for _ in range(xy_size)] for _ in range(xy_size)] for _ in range(z_size)]


for y in range(len(initial_layer)):
    for x in range(len(initial_layer[0])):
        cube[cycles][cycles + y][cycles + x] = initial_layer[y][x]

unit_vector = [-1, 0, 1]

for _ in range(cycles):
    for z in range(z_size):
        for y in range(xy_size):
            for x in range(xy_size):
                element = cube[z][y][x]
                active_elements = 0
                for v_z in unit_vector:
                    for v_y in unit_vector:
                        for v_x in unit_vector:
                            try:
                                if cube[z + v_z][y + v_y][x + v_x] == "#" and [v_x, v_y, v_z] != [0, 0, 0]:
                                    active_elements += 1
                            except IndexError:
                                pass
                if element == "." and active_elements == 3:
                    new_cube[z][y][x] = "#"
                if element == "#" and active_elements in [2, 3]:
                    new_cube[z][y][x] = "#"
                elif element == "#":
                    new_cube[z][y][x] = "."
    cube = [[[element for element in line] for line in layer] for layer in new_cube]


num_of_active_elements = 0

for layer in cube:
    for line in layer:
        for element in line:
            if element == "#":
                num_of_active_elements += 1
print(num_of_active_elements)

# part 2
# order - z, y, x, w
w_size = z_size
cube = [[[["." for _ in range(xy_size)] for _ in range(xy_size)] for _ in range(z_size)] for _ in range(w_size)]
new_cube = [[[["." for _ in range(xy_size)] for _ in range(xy_size)] for _ in range(z_size)] for _ in range(w_size)]

for y in range(len(initial_layer)):
    for x in range(len(initial_layer[0])):
        cube[cycles][cycles][cycles + y][cycles + x] = initial_layer[y][x]

unit_vector = [-1, 0, 1]

active_elements = 0
xy_product = [x for x in range(xy_size)]
zw_product = [z for z in range(z_size)]

for _ in range(cycles):
    for x, y, z, w in itertools.product(xy_product, xy_product, zw_product, zw_product):
        element = cube[w][z][y][x]
        active_elements = 0
        for dx, dy, dz, dw in itertools.product(unit_vector, repeat=4):
            try:
                if cube[w + dw][z + dz][y + dy][x + dx] == "#" and [dw, dz, dy, dx] != [0, 0, 0, 0]:
                    active_elements += 1
            except IndexError:
                pass
        if element == "." and active_elements == 3:
            new_cube[w][z][y][x] = "#"
        if element == "#" and active_elements in [2, 3]:
            new_cube[w][z][y][x] = "#"
        elif element == "#":
            new_cube[w][z][y][x] = "."
    cube = copy.deepcopy(new_cube)
    print("cycle")

num_of_active_elements = 0
for x, y, z, w in itertools.product(xy_product, xy_product, zw_product, zw_product):
    element = cube[w][z][y][x]
    if element == "#":
        num_of_active_elements += 1

print(num_of_active_elements)
