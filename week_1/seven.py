from collections import defaultdict, deque


def part_one(lines):
    rules = {}
    for line in lines:
        s = line.strip().split(" bags contain ")
        content = defaultdict(int)
        for comp in s[1].split(", "):
            words = comp.split(" ")
            if words[0] != "no":
                content[words[1] + " " + words[2]] = int(words[0])
        rules[s[0]] = content

    bags = set(["shiny gold"])
    l = 0
    while len(bags) > l:
        l = len(bags)
        for key in rules:
            if any(color in rules[key] for color in bags):
                bags.add(key)
    return len(bags) - 1, rules


def part_two(lines, rules):
    bags = defaultdict(int)
    q = deque([("shiny gold", 1)])
    while len(q) > 0:
        color, amount = q.pop()
        for key in rules[color]:
            q.append((key, rules[color][key] * amount))
            bags[key] += rules[color][key] * amount
    return sum(bags.values())


if __name__ == "__main__":
    with open("input7.txt") as f:
        lines = [line.strip() for line in f]
    res, rules = part_one(lines)
    print(res)
    print(part_two(lines, rules))
