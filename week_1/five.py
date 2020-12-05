def part_one(lines):
    seat_ids = list()
    for line in lines:
        line = line.translate(str.maketrans("FLBR", "0011"))
        row = int(line[:7], 2)
        column = int(line[7:], 2)
        seat_ids.append(row * 8 + column)
    seat_ids = sorted(seat_ids)
    return seat_ids, seat_ids[-1]


def part_two(seat_ids):
    all_ids = range(seat_ids[0], seat_ids[-1])
    return set(all_ids).difference(seat_ids)


if __name__ == "__main__":
    with open("input5.txt") as f:
        lines = [line.strip() for line in f]
    seat_ids, max_seatid = part_one(lines)
    print("Part 1: {}".format(max_seatid))
    my_id = part_two(seat_ids)
    print("Part 2: {}".format(my_id))
