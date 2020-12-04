if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = [int(line) for line in f]
    lens = len(numbers)
    for i in range(lens):
        for j in range(i + 1, lens):
            for k in range(j + 1, lens):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(numbers[i], numbers[j], numbers[k])
                    print("mul:", numbers[i] * numbers[j] * numbers[k])
