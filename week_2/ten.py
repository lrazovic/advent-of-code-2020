def part_one(nums: list[int]):
    delta = [nums[i] - nums[i - 1] for i in range(len(nums))]
    return delta.count(1) * delta.count(3)


def part_two(nums: list[int]):
    nums.reverse()
    path = {x: -1 for x in nums}
    path[nums[0]] = 1
    for key in path:
        if key != nums[0]:
            sum = 0
            for x in range(1,4):
                if key + x in path:
                    sum += path[key + x]
            path[key] = sum
    return path[0]


if __name__ == "__main__":
    with open("input10.txt") as f:
        nums = sorted([0] + [int(line) for line in f])
        nums.append(nums[-1] + 3)
    print(f"Part 1: {part_one(nums)}")
    print(f"Part 2: {part_two(nums)}")
