import math


def part_one(buses, earliest):
    return math.prod(min((bus[1] - earliest % bus[1], bus[1]) for bus in buses))


def part_two(buses):
    time, step = 0, 1
    for offset, bus in buses:
        while (time + offset) % bus:
            time += step
        step *= bus
    return time


if __name__ == "__main__":
    with open("input13.txt") as file:
        earliest = int(file.readline())
        buses = [
            (index, int(bus))
            for index, bus in enumerate(file.readline().split(","))
            if bus != "x"
        ]
    print(f"Part 1: {part_one(buses, earliest)}")
    print(f"Part 2: {part_two(buses)}")
