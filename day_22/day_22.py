from copy import deepcopy


def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    player_1, player_2 = [], []
    active_player = 1
    for i, line in enumerate(lines[1:-2]):
        if line == "\n":
            active_player = 2
        if active_player == 1:
            player_1.append(int(line))
        else:
            player_2.append(int(lines[i + 3]))
    return player_1, player_2


p1_deck, p2_deck = read_input()


# part 1
while p1_deck and p2_deck:
    if p1_deck[0] > p2_deck[0]:
        p1_deck.extend([p1_deck[0], p2_deck[0]])
    else:
        p2_deck.extend([p2_deck[0], p1_deck[0]])
    del p1_deck[0], p2_deck[0]

result = 0
for i, card in enumerate(p1_deck[::-1]):
    result += (i + 1) * card
print(result)


# part 2


def recursive_game(p1_deck, p2_deck):
    iter = 0
    decks = []
    while p1_deck and p2_deck:
        iter += 1
        if p1_deck + p2_deck in decks:
            return 1, p1_deck, p2_deck
        decks.append(p1_deck + p2_deck)
        if p1_deck[0] < len(p1_deck) and p2_deck[0] < len(p2_deck):
            winner = recursive_game(deepcopy(p1_deck[1 : p1_deck[0] + 1]), deepcopy(p2_deck[1 : p2_deck[0] + 1]))[0]
            if winner == 1:
                p1_deck.extend([p1_deck[0], p2_deck[0]])
            else:
                p2_deck.extend([p2_deck[0], p1_deck[0]])
        elif p1_deck[0] > p2_deck[0]:
            p1_deck.extend([p1_deck[0], p2_deck[0]])
        else:
            p2_deck.extend([p2_deck[0], p1_deck[0]])
        del p1_deck[0], p2_deck[0]
    if p1_deck:
        return 1, deepcopy(p1_deck), deepcopy(p2_deck)
    else:
        return 2, deepcopy(p1_deck), deepcopy(p2_deck)


p1_deck, p2_deck = read_input()
_, p1_deck, p2_deck = recursive_game(p1_deck, p2_deck)
result = 0
print(p1_deck, p2_deck)
for i, card in enumerate(p1_deck[::-1] + p2_deck[::-1]):
    result += (i + 1) * card
print(result)
