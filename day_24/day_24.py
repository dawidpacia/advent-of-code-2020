def read_input():
    with open("input.txt") as line:
        lines = line.readlines()
    tiles_directions = []
    for line in lines:
        tile_directions = []
        skip_next = False
        for i, letter in enumerate(line):
            if letter in ["e", "w"] and not skip_next:
                tile_directions.append(letter)
            skip_next = False
            if letter in ["n", "s"]:
                tile_directions.append(line[i : i + 2])
                skip_next = True
        tiles_directions.append(tile_directions)
    return tiles_directions


tiles = read_input()

directions_map = {"ne": (1, 2), "nw": (-1, 2), "se": (1, -2), "sw": (-1, -2), "e": (2, 0), "w": (-2, 0)}
tiles_position = {}
current_boundaries = [0, 0, 0, 0]

for tile in tiles:
    final_position = [0, 0]
    for direction in tile:
        final_position = [x + y for x, y in zip(final_position, directions_map[direction])]
    final_position = "{} {}".format(final_position[0], final_position[1])
    if str(final_position) in tiles_position:
        tiles_position[final_position] = "white" if tiles_position[str(final_position)] == "black" else "black"
    else:
        tiles_position[final_position] = "black"

black_tiles = 0
for colour in tiles_position.values():
    if colour == "black":
        black_tiles += 1
print(black_tiles)

# part 2
new_tiles_position = tiles_position.copy()
for i in range(100):
    for position, colour in tiles_position.items():
        x, y = list(map(int, position.split()))
        adjusted_black = 0
        if tiles_position[position] == "white":
            continue

        # black check
        for vector in directions_map.values():
            adjusted_key = "{} {}".format(x + vector[0], y + vector[1])
            if adjusted_key in tiles_position.keys():
                if tiles_position[adjusted_key] == "black":
                    adjusted_black += 1
        if adjusted_black == 0 or adjusted_black > 2:
            new_tiles_position[position] = "white"

        # adjusted white check
        for adjusted_vector in directions_map.values():
            adjusted_black = 0
            x_adj = x + adjusted_vector[0]
            y_adj = y + adjusted_vector[1]
            for vector in directions_map.values():
                adjusted_key = "{} {}".format(x_adj + vector[0], y_adj + vector[1])
                if adjusted_key in tiles_position.keys():
                    if tiles_position[adjusted_key] == "black":
                        adjusted_black += 1
            if adjusted_black == 2:
                new_tiles_position["{} {}".format(x_adj, y_adj)] = "black"
    tiles_position = new_tiles_position.copy()

black_tiles = 0
for colour in tiles_position.values():
    if colour == "black":
        black_tiles += 1
print(black_tiles)
