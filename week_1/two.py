def part_one(lines):
    count = 0
    for line in lines:
        min_range, max_range = map(int, line[0].split("-"))
        letter = line[1][0]
        occurances = line[2].count(letter)
        if min_range <= occurances <= max_range:
            count += 1
    print(count)


def part_two(lines):
    count = 0
    for line in lines:
        first_pos, second_pos = map(int, line[0].split("-"))
        letter = line[1][0]
        word = line[2]
        if len(word) <= second_pos - 1:
            continue
        if (word[first_pos - 1] == letter) ^ (word[second_pos - 1] == letter):
            count += 1
    print(count)


if __name__ == "__main__":
    with open("input2.txt") as f:
        lines = [line.strip().split() for line in f]
    part_one(lines)
    part_two(lines)
