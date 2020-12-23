import re


def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()

    tile_map, tile_image, tile_id = {}, [], None
    for line in lines:
        if "Tile" in line:
            tile_id = re.findall("\d+", line)[0]
        elif line == "\n":
            tile_map[tile_id] = tile_image
            tile_image = []
        else:
            tile_image.append(line.strip())
    return tile_map


def extract_edges(image):
    edges = []
    # order left, top, right, bottm, flipped. left, f. top, f. right, f. bottom
    edges.extend([image[0][::-1], image[0], image[-1][::-1], image[-1]])
    top_flipped_edge, bottom_flipped_edge = "".join(line[0] for line in image), "".join(line[-1] for line in image)
    edges.extend([top_flipped_edge[::-1], top_flipped_edge, bottom_flipped_edge[::-1], bottom_flipped_edge])
    return edges


tile_map = read_input()
tile_edges = {}

for tile_id, image in tile_map.items():
    tile_edges[tile_id] = extract_edges(image)

intersected_edges_map = {}
for tile in tile_map:
    intersected_edges = 0
    for compared_tile, edges in tile_edges.items():
        if compared_tile != tile:
            intersected_edges += len(list(set(tile_edges[tile]) & set(edges))) // 2
    intersected_edges_map[tile] = intersected_edges

result = 1
for tile_id, value in intersected_edges_map.items():
    if value == 2:
        first_tile = tile_id
        result *= int(tile_id)

print(result)

# 1st tile setup
