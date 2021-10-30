import itertools
import functools

def from_file(path):
    entries = list()
    with open(path, "r") as file:
        parse_int = lambda string: int(string.strip())
        entries = [parse_int(string) for string in file.readlines()]
    return entries

def product(items):
    product = lambda x, y: x * y
    return functools.reduce(product, items)

def find_by_sum(entries, entries_to_sum = 2, value = 2020):
    result = list()
    combinations = itertools.combinations(entries, entries_to_sum)
    for combination in combinations:
        if(sum(combination) == 2020):
            result.append(product(combination))

    return result

if __name__ == "__main__":
    entries = from_file("input/day_01.txt")
    [part_01] = find_by_sum(entries)
    print("part_01:-", part_01)

    [part_02] = find_by_sum(entries, entries_to_sum = 3)
    print("part_02:-", part_02)
