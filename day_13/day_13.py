from functools import reduce


def read_input():
    with open("input.txt") as report_data:
        lines = report_data.readlines()
    notes = [line.strip() for line in lines]
    timestamp = int(notes[0])
    buses = notes[1].split(",")
    return timestamp, buses


def get_closest_time(timestamp, valid_buses, timestamp_limit=10000000):
    for current_time in range(timestamp, timestamp_limit):
        for bus in valid_buses:
            if current_time % bus == 0:
                return current_time, bus
    return False


def check_bus_at_timestamp(timestamp, bus, offset):
    if (timestamp + offset) % bus:
        return False
    return True


timestamp, buses = read_input()


# part 1
valid_buses = [int(bus) for bus in buses if bus != "x"]
current_timestamp, bus_nr = get_closest_time(timestamp, valid_buses)
print((current_timestamp - timestamp) * bus_nr)


# part 2
valid_buses_idx = [[int(bus), int(bus) - idx] for idx, bus in enumerate(buses) if bus != "x"]

# Using Chinese remainder theorem
b_i, N_i, x_i, bNx_i = [], [], [], []
N = reduce(lambda x, y: x * y, valid_buses)
for bus, idx in valid_buses_idx:
    b_i.append(idx)
    N_i.append(int(N / bus))
    x_iter = 1
    while (N_i[-1] * x_iter) % bus != 1:
        x_iter += 1
    x_i.append(x_iter)
    bNx_i.append(b_i[-1] * N_i[-1] * x_i[-1])

x = int(sum(bNx_i))
print(x % N)
