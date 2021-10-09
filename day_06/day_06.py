Answer = dict[str, int]

def new_group(string: str, group: Answer = Answer()) -> Answer:
    for letter in string:
        if(letter not in group):
            group[letter] = 1
        else:
            group[letter] += 1
    return group

def new_groups(path: str) -> list[Answer]:
    groups = list[Answer]({})
    group_id = 0
    group_size = 1
    lines = [line.strip() for line in open(path, "r")]

    for line in lines:
        if(line == ''):
            groups[group_id].update({"size": group_size})
            group_size = 1
            group_id += 1
        elif((group_id + 1) != len(groups)):
            groups.append(new_group(line, Answer()))
        else:
            group = groups[group_id]
            new_group(line, group)
            group_size += 1
    else:
        groups[group_id].update({"size": group_size})

    return groups

def count_anyone_yes(groups: list[Answer]) -> int:
    count = 0
    for group in groups:
        for letter in group.keys():
            if(letter != "size"):
                count += 1
    return count

def count_everyone_yes(groups: list[Answer]) -> int:
    count = 0
    for group in groups:
        for letter in group.keys():
            if(letter != "size"):
                if(group[letter] == group["size"]):
                    count += 1
    return count

if __name__ == "__main__":
    groups = new_groups("input/day_06.txt")
    part_01 = count_anyone_yes(groups)
    print("part_01:-", part_01)

    part_02  = count_everyone_yes(groups)
    print("part_02:-", part_02)
