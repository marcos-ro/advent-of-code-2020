import typing
import re

T = typing.TypeVar("T")
Password = dict[str, T]
regex = re.compile("^\d+\-\d+\s\w:\s\w*$")

def new_password(string: str) -> Password:
    password = dict[str, T]()
    if(regex.search(string)):
        [string_range, character, plain] = string.replace(":", "").split(" ")
        password["range"] = tuple([int(item) for item in string_range.split("-")])
        password["character"]  = character
        password["plain"] = plain

    return password

def new_passwords(path: str) -> list[Password]:
    lines = open(path, "r").readlines()
    return [new_password(line.strip()) for line in lines]

def default_policy(password: Password) -> bool:
    count = password["plain"].count(password["character"])
    (count_min, count_max) = password["range"]
    return (count >= count_min) and (count <= count_max)
    
def new_policy(password: Password) -> bool:
    (begin, end) = password["range"]
    character = password["character"]
    plain = password["plain"]
    return (plain[begin-1] == character) ^ (plain[end-1] == character)

def count_by_policy(passwords: list[Password], policy: typing.Callable[Password, bool]) -> int:
    valid_passwords = 0
    for password in passwords:
        if(policy(password)):
            valid_passwords += 1

    return valid_passwords

if __name__ == "__main__":
    passwords = new_passwords("input/day_02.txt")
    part_01 = count_by_policy(passwords, default_policy)
    print("part_01:-", part_01)

    part_02 = count_by_policy(passwords, new_policy)
    print("part_02:-", part_02)
