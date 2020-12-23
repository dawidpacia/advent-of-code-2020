import itertools


def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    products = []
    for line in lines:
        ingredients, allergens = line.strip().split("(contains")
        ingredients = set(ingredients.split())
        allergens = set(allergens.strip().replace(")", "").split(", "))
        products.append([ingredients, allergens])
    return products


products = read_input()
allergens_map = {}
all_ingredients = []
unique_ingredients = set()
ingredients_with_allergen = set()

for ingredients, allergens in products:
    all_ingredients.extend(ingredients)
    unique_ingredients = unique_ingredients.union(ingredients)
    for allergen in allergens:
        if allergen not in allergens_map.keys():
            allergens_map[allergen] = ingredients
        else:
            common_ingredients = ingredients.intersection(allergens_map[allergen])
            allergens_map[allergen] = common_ingredients

for allergen_ingredients in allergens_map.values():
    ingredients_with_allergen = ingredients_with_allergen.union(allergen_ingredients)

# part 1
num_of_appearances = 0
for ingredient in unique_ingredients:
    if ingredient not in ingredients_with_allergen:
        num_of_appearances += all_ingredients.count(ingredient)

print(num_of_appearances)

# part 2
while len(allergens_map) != len(list(itertools.chain.from_iterable(allergens_map.values()))):
    for allergen, ingredients in allergens_map.items():
        if len(ingredients) == 1:
            for iter_allergen, iter_ingredients in allergens_map.items():
                if (
                    allergen != iter_allergen
                    and len(iter_ingredients) != 1
                    and ingredients.intersection(iter_ingredients)
                ):
                    allergens_map[iter_allergen].discard(list(ingredients)[0])

dangerous_ingredients_list = []
for key, value in sorted(allergens_map.items()):
    dangerous_ingredients_list.append(list(value)[0])

print(",".join(dangerous_ingredients_list))
