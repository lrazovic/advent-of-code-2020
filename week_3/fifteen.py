from collections import defaultdict


def both_parts(numbers, limit):
	hist = defaultdict(lambda: index)
	last = 0
	for index, number in enumerate(numbers):
		hist[last], last = index, number
	for index in range(len(numbers), limit):
		hist[last], last = index, index - hist[last]
	return last


if __name__ == "__main__":
	with open("input15.txt") as f:
		lines = [int(line) for line in f.read().split(",")]
	print(f"Part 1: {both_parts(lines, 2020)}")
	print(f"Part 2: {both_parts(lines, 30000000)}")
