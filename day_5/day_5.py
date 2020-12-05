def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    seats = [(line.strip()) for line in lines if line.strip()]
    return seats


def calculate_seat(chars: str):
    bin_row = chars[:7].replace("F", "0").replace("B", "1")
    bin_column = chars[-3:].replace("L", "0").replace("R", "1")
    return int(bin_row, 2), int(bin_column, 2)


def get_seat_id(row, column):
    return row * 8 + column


seats_hex = read_input()

# part 1
seats = []
seats_id = []
for seat in seats_hex:
    row, column = calculate_seat(seat)
    seat_id = get_seat_id(row, column)
    seats.append((row, column))
    seats_id.append(seat_id)

print(max(seats_id))

# part 2
seat_offset = 30
for row in range(seat_offset, 128 - seat_offset):
    for column in range(8):
        if (row, column) not in seats:
            print(row, column)
            your_place = row, column

print(get_seat_id(*your_place))
