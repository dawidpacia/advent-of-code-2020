def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    tree_map = [(line.strip()) for line in lines if line.strip()]
    return tree_map


def count_trees(tree_map, step_x, step_y):
    x_len, y_len = len(tree_map[0]), len(tree_map)
    pointer_x, pointer_y = 0, 0
    num_of_trees = 0

    for _ in range(0, y_len, step_y):
        if tree_map[pointer_y][pointer_x % x_len] == "#":
            num_of_trees += 1
        pointer_x += step_x
        pointer_y += step_y
    return num_of_trees


tree_map = read_input()
movement_schemas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

total_trees_mul = 1
for schema in movement_schemas:
    total_trees_mul *= count_trees(tree_map, *schema)

print(total_trees_mul)
