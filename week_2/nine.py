def valid(nums, n):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == n:
                return True
    return False


def part_one(nums):
    for i in range(25, len(nums)):
        if not valid(nums[i - 25 : i], nums[i]):
            return nums[i]


def part_two(nums, target):
    sset = dict()
    rsum = 0
    for index, num in enumerate(nums):
        sset[rsum] = index
        rsum += num
        if rsum - target in sset:
            lo = sset[rsum - target]
            vals = nums[lo : index + 1]
            return min(vals) + max(vals)


if __name__ == "__main__":
    with open("input9.txt") as f:
        nums = [int(line) for line in f]
    target = part_one(nums)
    print(f"Part 1: {target}")
    print(f"Part 2: {part_two(nums, target)}")
