from collections import deque


def part_one(instructions):
    res, ip = 0, 0
    seen = set()
    history = deque()
    while True:
        if ip >= len(instructions):
            return (0, res, history)
        elif ip in seen:
            return (-1, res, history)
        else:
            seen.add(ip)
        op, arg = instructions[ip]
        history.appendleft((ip, (op, arg)))
        if op == 0:
            ip += 1
        elif op == 1:
            res += arg
            ip += 1
        elif op == 2:
            ip += arg


def part_two(hist, instructions):
    while hist:
        i, (op, arg) = hist.popleft()
        if op % 2 == 0:
            mod_code = instructions
            mod_code[i] = ((op + 2) % 4, arg)
            return_code, res, _ = part_one(mod_code)
            if return_code == 0:
                return res


if __name__ == "__main__":
    commands = {"nop": 0, "acc": 1, "jmp": 2}
    with open("input8.txt") as f:
        instructions = [(commands[line[:3]], int(line[3:])) for line in f]
    _, res, history = part_one(instructions)
    part2 = part_two(history, instructions)
    print(f"Part 1: {res}")
    print(f"Part 2: {part2}")
