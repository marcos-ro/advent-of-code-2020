import typing
import re

T = typing.TypeVar("T")
Passport = dict[str, str]
hgt_re = re.compile("^\d+(cm|in)$")
hcl_re = re.compile("^#[0-9abcdef]{6}$")
pid_re = re.compile("^\d{9}$")


def new_passport(string: str) -> Passport:
    passport = Passport()
    for items in string.split("\n"):
        for item in items.split(" "):
            if(len(item) > 0):
                find_dot = item.find(":")
                key = item[0:find_dot]
                value = item[find_dot+1:]
                passport[key] = value

    return passport

def new_passports(path: str) -> list[Passport]:
    lines = open(path, "r").readlines()
    passport = Passport()
    passports = list[Passport]()
    for line in lines:
        if(line == "\n"):
            passports.append(passport.copy())
            passport = Passport()
        else:
            passport.update(new_passport(line)) 
    else:
        passports.append(passport.copy())

    return passports

def default_policy(passport: Passport) -> bool:
    return (len(passport) == 8) or ((len(passport) == 7) and ("cid" not in passport))

def new_policy(passport: Passport) -> bool:
    count_valid_policy = 0
    if(default_policy(passport)):
        if(passport["byr"].isnumeric()):
            byr = int(passport["byr"])
            if((byr >= 1920) and (byr <= 2002)):
                count_valid_policy += 1

        if(passport["iyr"].isnumeric()):
            iyr = int(passport["iyr"])
            if((iyr >= 2010) and (iyr <= 2020)):
                count_valid_policy += 1

        if(passport["eyr"].isnumeric()):
            eyr = int(passport["eyr"])
            if((eyr >= 2020) and (eyr <= 2030)):
                count_valid_policy += 1

        if(hgt_re.search(passport["hgt"])):
            hgt = passport["hgt"]
            if("cm" in hgt):
                cm = int(hgt.replace("cm", ""))
                if((cm >= 150) and (cm <= 193)):
                    count_valid_policy += 1

            elif("in" in hgt):
                _in = int(hgt.replace("in", ""))
                if((_in >= 59) and (_in <= 76)):
                    count_valid_policy += 1

        if(hcl_re.search(passport["hcl"])):
            count_valid_policy += 1

        if(passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            count_valid_policy += 1

        if(pid_re.search(passport["pid"])):
            count_valid_policy += 1

    return count_valid_policy == 7

def count_by_policy(passports: list[Passport], policy: typing.Callable[Passport, bool]) -> int:
    count = 0
    for passport in passports:
        if(policy(passport)):
            count += 1

    return count

if __name__ == "__main__":
    passports = new_passports("input/day_04.txt")
    part_01 = count_by_policy(passports, default_policy)
    print("part_01:-", part_01)

    part_02 = count_by_policy(passports, new_policy)
    print("part_02:-", part_02)
