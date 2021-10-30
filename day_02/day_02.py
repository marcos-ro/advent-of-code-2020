
def from_file(path):
    passwords = list()
    with open(path, "r") as file:
        passwords = [parse_password(string) for string in file.readlines()]

    return passwords

def parse_password(string):
    password = dict()
    parse_int = lambda string: int(string)
    [string_range, character, plain] = string.replace(":", "").split(" ")
    password["range"] = tuple([parse_int(string) for string in string_range.split("-")])
    password["character"] = character
    password["plain"] = plain

    return password

def default_policy(password):
    count = password["plain"].count(password["character"])
    (count_min, count_max) = password["range"]
    return (count >= count_min) and (count <= count_max)
    
def new_policy(password):
    (begin, end) = password["range"]
    character = password["character"]
    plain = password["plain"]
    return (plain[begin-1] == character) ^ (plain[end-1] == character)

def count_by_policy(passwords, policy = default_policy):
    valid_passwords = int()
    for password in passwords:
        if(policy(password)):
            valid_passwords += 1

    return valid_passwords

if __name__ == "__main__":
    passwords = from_file("input/day_02.txt")
    part_01 = count_by_policy(passwords)
    print("part_01:-", part_01)

    part_02 = count_by_policy(passwords, new_policy)
    print("part_02:-", part_02)
