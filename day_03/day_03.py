
def from_file(path):
    grid = list()
    with open(path, "r") as file:
        grid = [string.strip() for string in file.readlines()]

    return grid

def simulate(grid, steps, three = int()):
    if(steps["y"] >= len(grid)):
        return three
    else:
        (new_steps, new_three) = processing_row(grid[steps["y"]], steps, three)
        return simulate(grid, new_steps, new_three)

def simulate_by_steps_list(grid, steps_list):
    product = 1
    for steps in steps_list:
        product *= simulate(grid, steps)

    return product

def processing_row(row, steps, three):
    x = steps["x"]
    row_size = len(row)
    steps["x"] += steps["right"]
    steps["y"] += steps["down"]
    if(row_size > x):
        new_three = count_three(row[x], three)
        return (steps, new_three)
    else:
        (new_steps, new_row) = repeat_row(row, steps)
        new_three = count_three(new_row[x], three)
        return (new_steps, new_three)

def repeat_row(row, steps):
    new_row = row * steps["repeat"]
    if(len(new_row) > steps["x"]):
        return (steps, new_row)
    else:
        steps["repeat"] += 2
        return repeat_row(new_row, steps)

def count_three(item, three):
    if(item == "#"):
        three += 1

    return three

if __name__ == "__main__":
    grid = from_file("input/day_03.txt")
    part_01_steps = {"right": 3, "down": 1, "x": 0, "y": 0, "repeat": 2}
    part_01 = simulate(grid, part_01_steps)
    print("part_01:-", part_01)

    part_02_steps = [
        {"right": 1, "down": 1, "x": 0, "y": 0, "repeat": 2},
        {"right": 3, "down": 1, "x": 0, "y": 0, "repeat": 2},
        {"right": 5, "down": 1, "x": 0, "y": 0, "repeat": 2},
        {"right": 7, "down": 1, "x": 0, "y": 0, "repeat": 2},
        {"right": 1, "down": 2, "x": 0, "y": 0, "repeat": 2},
    ]
    part_02 = simulate_by_steps_list(grid, part_02_steps)
    print("part_02:-", part_02) 
