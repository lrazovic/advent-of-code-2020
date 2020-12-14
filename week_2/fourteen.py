def write(memory, mask, address, value):
    if "X" in mask:
        i = mask.index("X")
        write(memory, mask[:i] + "0" + mask[i + 1 :], address, value)
        write(memory, mask[:i] + "1" + mask[i + 1 :], address, value)
    else:
        memory[int(mask, 2) | address] = value


def both_part(lines):
    m1 = {}
    m2 = {}
    mask = None
    for line in lines:
        key, value = line
        if key == "mask":
            mask = value
        else:
            address = int(key[4:-1])
            value = int(value)

            m1[address] = value & int(
                mask.replace("1", "0").replace("X", "1"), 2
            ) | int(mask.replace("X", "0"), 2)

            address &= int(mask.replace("0", "1").replace("X", "0"), 2)
            write(m2, mask, address, value)
    return sum(m1.values()), sum(m2.values())


if __name__ == "__main__":
    with open("input14.txt") as f:
        lines = [line.strip().split(" = ") for line in f]
    part1, part2 = both_part(lines)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
