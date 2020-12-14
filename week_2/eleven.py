import itertools
from copy import deepcopy


def part_one(seats):
    old_seats = None

    while old_seats != seats:
        old_seats = deepcopy(seats)

        for row in range(len(old_seats)):
            for col in range(len(old_seats[0])):
                if old_seats[row][col] == ".":
                    continue

                occupied_count = sum(
                    old_seats[row + x][col + y] == "#"
                    for x, y in itertools.product((-1, 0, 1), repeat=2)
                    if (x, y) != (0, 0)
                )

                if occupied_count == 0:
                    seats[row][col] = "#"
                elif occupied_count >= 4:
                    seats[row][col] = "L"
    return sum(row.count("#") for row in seats)


def part_two(seats):
    old_seats = None
    while old_seats != seats:
        old_seats = deepcopy(seats)

        for row in range(len(old_seats)):
            for col in range(len(old_seats[0])):
                if old_seats[row][col] in ".X":
                    continue

                total = 0
                for x, y in itertools.product((-1, 0, 1), repeat=2):
                    if (x, y) == (0, 0):
                        continue

                    for scale in itertools.count(1):
                        seat = old_seats[row + scale * x][col + scale * y]

                        if seat != ".":
                            total += seat == "#"
                            break

                if total == 0:
                    seats[row][col] = "#"
                elif total >= 5:
                    seats[row][col] = "L"

    return sum(row.count("#") for row in seats)


if __name__ == "__main__":
    with open("input11.txt") as f:
        seats_1 = [list("." + line.strip() + ".") for line in f]
        seats_1 = [["."] * len(seats_1[0])] + seats_1 + [["."] * len(seats_1[0])]
    with open("input11.txt") as f:
        seats_2 = [list("X" + line.strip() + "X") for line in f]
        seats_2 = [["X"] * len(seats_2[0])] + seats_2 + [["X"] * len(seats_2[0])]
    print(f"Part 1: {part_one(seats_1)}")
    print(f"Part 2: {part_two(seats_2)}")
