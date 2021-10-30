import re

hgt_re = re.compile("^\d+(cm|in)$")
hcl_re = re.compile("^#[0-9abcdef]{6}$")
pid_re = re.compile("^\d{9}$")

def from_file(path):
    passports = list()
    with open(path, "r") as file:
        passport = dict()
        for string in file.readlines():
            if(string == "\n"):
                passports.append(passport.copy())
                passport = dict()
            else:
                passport.update(parse_passport(string))
        else:
            passports.append(passport.copy())

    return passports

def parse_passport(string):
    passport = dict()
    for items in string.split("\n"):
        for item in items.split(" "):
            if(len(item) > 0):
                find_dot = item.find(":")
                key = item[0:find_dot]
                value = item[find_dot+1:]
                passport[key] = value

    return passport

def default_policy(passport):
    size = len(passport)
    return (size == 8) or ((size == 7) and ("cid" not in passport))

def parse_int(string):
    return int(string)

def is_valid_byr(string):
    result = bool()
    if(string.isnumeric()):
        byr = parse_int(string)
        result = (byr >= 1920) and (byr <= 2002)

    return result

def is_valid_iyr(string):
    result = bool()
    if(string.isnumeric()):
        iyr = parse_int(string)
        result = (iyr >= 2010) and (iyr <= 2020)

    return result

def is_valid_eyr(string):
    result = bool()
    if(string.isnumeric()):
        eyr = parse_int(string)
        result = (eyr >= 2020) and (eyr <= 2030)

    return result

def is_valid_hgt(string):
    result = bool()
    if(hgt_re.search(string)):
        if("cm" in string):
            cm = parse_int(string.replace("cm", ""))
            result = (cm >= 150) and (cm <= 193)
        elif("in" in string):
            _in = parse_int(string.replace("in", ""))
            result = (_in >= 59) and (_in <= 76)

    return result

def is_valid_hcl(string):
    return hcl_re.search(string)

def is_valid_ecl(string):
    return string in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def is_valid_pid(string):
    return pid_re.search(string)

def new_policy(passport):
    count_valid_policy = int()
    if(default_policy(passport)):
        is_valid = {
            "byr": is_valid_byr,
            "iyr": is_valid_iyr,
            "eyr": is_valid_eyr,
            "hgt": is_valid_hgt,
            "hcl": is_valid_hcl,
            "ecl": is_valid_ecl,
            "pid": is_valid_pid
        }

        for key in passport.keys():
            if(key != "cid"):
                validate = is_valid[key]
                string = passport[key]
                if(validate(string)):
                    count_valid_policy += 1

    return count_valid_policy == 7

def count_by_policy(passports, policy = default_policy):
    count = int()
    for passport in passports:
        if(policy(passport)):
            count += 1

    return count

if __name__ == "__main__":
    passports = from_file("input/day_04.txt")
    part_01 = count_by_policy(passports)
    print("part_01:-", part_01)

    part_02 = count_by_policy(passports, new_policy)
    print("part_02:-", part_02)
