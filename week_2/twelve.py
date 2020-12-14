def both_part(instructions, waypoint=1 + 0j):
    actions = {"N": 1j, "S": -1j, "E": 1, "W": -1}
    position = 0 + 0j
    waypoint_mode = waypoint != 1 + 0j

    for action, value in instructions:
        if action == "L":
            waypoint *= pow(1j, value // 90)
        elif action == "R":
            waypoint *= pow(-1j, value // 90)
        elif action == "F":
            position += waypoint * value
        elif waypoint_mode:
            waypoint += actions[action] * value
        else:
            position += actions[action] * value

    return int(abs(position.real) + abs(position.imag))


if __name__ == "__main__":
    with open("input12.txt") as f:
        instructions = [(line[0], int(line[1:])) for line in f]
    print(f"Part 1: {both_part(instructions)}")
    print(f"Part 2: {both_part(instructions, 10+1j)}")
