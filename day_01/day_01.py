import itertools
import functools

def new_entries(path: str) -> list[int]:
    lines = open(path, "r").readlines()
    return [int(line.strip()) for line in lines if line.strip().isnumeric()]

def product(values: list[int]) -> int:
    return functools.reduce(lambda x, y: x * y, values)

def find_by_sum(entries: list[int], entries_to_sum: int, value: int) -> list[int]:
    result: List[int] = list()
    combinations = itertools.combinations(entries, entries_to_sum)
    for combination in combinations:
        if(sum(combination) == 2020):
            result.append(product(list(combination)))

    return result

if __name__ == "__main__":
    entries = new_entries("input/day_01.txt")
    [part_01] = find_by_sum(entries, 2, 2020)
    print("part_01:-", part_01)

    [part_02] = find_by_sum(entries, 3, 2020)
    print("part_02:-", part_02)
