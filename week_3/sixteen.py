import re

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


def part_one(lines, ranges, nearby):
    valid = set()
    for t1, t2, t3, t4 in ranges:
        valid |= set(range(t1, t2 + 1))
        valid |= set(range(t3, t4 + 1))
    return sum(n for l in nearby for n in l if n not in valid), valid


def part_two(lines, ranges, nearby, valid):
    valids = [l for l in nearby if all(n in valid for n in l)]
    loc = [
        [
            all((t1 <= l[j] <= t2) or (t3 <= l[j] <= t4) for l in valids)
            for t1, t2, t3, t4 in ranges
        ]
        for j in range(20)
    ]
    m = maximum_bipartite_matching(csr_matrix(loc))
    return your[m[:6]].prod()


if __name__ == "__main__":
    with open("input16.txt") as f:
        lines = [line.strip() for line in f]
        ranges = [list(map(int, re.findall(r"\d+", x))) for x in lines[:20]]
        your = np.array([int(x) for x in lines[22].split(",")])
        nearby = [list(map(int, re.findall(r"\d+", x))) for x in lines[25:]]
    part_1, valid = part_one(lines, ranges, nearby)
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_two(lines, ranges, nearby, valid)}")
