
def from_file(path):
    with open(path, "r") as file:
        groups = list({})
        group_id = int()
        group_size = 1

        for string in file.readlines():
            string = string.strip()
            if(string == ''):
                groups[group_id].update({"size": group_size})
                group_size = 1
                group_id += 1
            elif((group_id + 1) != len(groups)):
                groups.append(parse_group(string, dict()))
            else:
                group = groups[group_id]
                parse_group(string, group)
                group_size += 1
        else:
            groups[group_id].update({"size": group_size})

        return groups


def parse_group(string, group = dict()):
    for letter in string:
        if(letter not in group):
            group[letter] = 1
        else:
            group[letter] += 1
    return group

def count_anyone_yes(groups):
    count = int()
    for group in groups:
        for letter in group.keys():
            if(letter != "size"):
                count += 1
    return count

def count_everyone_yes(groups):
    count = int()
    for group in groups:
        for letter in group.keys():
            if(letter != "size"):
                if(group[letter] == group["size"]):
                    count += 1
    return count

if __name__ == "__main__":
    groups = from_file("input/day_06.txt")
    part_01 = count_anyone_yes(groups)
    print("part_01:-", part_01)

    part_02  = count_everyone_yes(groups)
    print("part_02:-", part_02)
