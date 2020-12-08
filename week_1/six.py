def part_one(blocks):
    return sum(len(set.union(*map(set, group.split()))) for group in blocks)


def part_two(blocks):
    return sum(len(set.intersection(*map(set, group.split()))) for group in blocks)


if __name__ == "__main__":
    with open("input6.txt") as f:
        blocks = f.read().split("\n\n")
    print("Part 1: {}".format(part_one(blocks)))
    print("Part 2: {}".format(part_two(blocks)))
