import re


def get_passport(data):
    passport = dict()
    fields = [field for field in data.split()]
    for field in fields:
        key, value = field.split(":")
        passport[key] = value
    return passport


validate_byr = lambda byr: len(byr) == 4 and 1920 <= int(byr) <= 2002
validate_iyr = lambda iyr: len(iyr) == 4 and 2010 <= int(iyr) <= 2020
validate_eyr = lambda eyr: len(eyr) == 4 and 2020 <= int(eyr) <= 2030
validate_ecl = lambda ecl: ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
validate_pid = lambda pid: re.match(r"^[0-9]{9}$", pid)
validate_hcl = lambda hcl: re.match(r"^#[a-f0-9]{6}$", hcl)


def validate_hgt(hgt):
    valid = False
    if hgt.endswith("cm"):
        valid = 150 <= int(hgt[:-2]) <= 193
    elif hgt.endswith("in"):
        valid = 59 <= int(hgt[:-2]) <= 76
    return valid


def part_one(passport):
    fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    return all(field in passport.keys() for field in fields)


def part_two(passport):
    try:
        assert part_one(passport)
        assert validate_byr(passport["byr"])
        assert validate_iyr(passport["iyr"])
        assert validate_eyr(passport["eyr"])
        assert validate_hgt(passport["hgt"])
        assert validate_hcl(passport["hcl"])
        assert validate_ecl(passport["ecl"])
        assert validate_pid(passport["pid"])
        return True
    except:
        return False


if __name__ == "__main__":
    with open("input4.txt") as f:
        passports = [get_passport(block) for block in f.read().split("\n\n")]
    print("Part 1: {}".format(sum(part_one(passport) for passport in passports)))
    print("Part 2: {}".format(sum(part_two(passport) for passport in passports)))
