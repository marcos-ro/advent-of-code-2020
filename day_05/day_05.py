import typing
import math

T = typing.TypeVar("T")
Compute = dict[str, T]
Seat = (int, int)

def from_file(path):
    boarding_passes = list()
    with open(path, "r") as file:
        boarding_passes = [string.strip() for string in file.readlines()]
        
    return boarding_passes

def processing_letter(letter, compute):
    processing = compute.copy()
    if(letter in ["F", "B"]):
        rows = processing["rows"]
        rows_keeping = processing["rows_keeping"]
        rows_mean = (rows + rows_keeping) / 2
        if(letter == "F"):
            processing["rows"] = math.floor(rows_mean)
        else:
            processing["rows_keeping"] = math.ceil(rows_mean)
    elif(letter in ["L", "R"]):
        column = processing["column"]
        column_keeping = processing["column_keeping"]
        column_mean = (column + column_keeping) / 2
        if(letter == "L"):
            processing["column"] = math.floor(column_mean)
        else:
            processing["column_keeping"] = math.ceil(column_mean)

    return processing

def parse_seat(boarding_pass):
    compute = {"rows": 127, "rows_keeping": 0, "column": 7, "column_keeping": 0}
    for letter in boarding_pass:
        compute.update(processing_letter(letter, compute))
    return (compute["rows_keeping"], compute["column_keeping"])

def calculate_id(boarding_pass: str) -> int:
    (row, column) = parse_seat(boarding_pass)
    return row * 8 + column

def calculate_max_id(boarding_passes):
    ids = [calculate_id(boarding_pass) for boarding_pass in boarding_passes]
    return max(ids)

def combinations():
    for column in range(1, 8):
        for row in range(1, 128):
            yield (row, column)

def my_seat(boarding_passes):
    _id = lambda seat: seat[0] * 8 + seat[1]
    used_seats = [parse_seat(boarding_pass) for boarding_pass in boarding_passes]
    all_seats = [_id(seat) for seat in combinations() if seat not in used_seats]
    return [seat for seat in all_seats if ((seat - 1) not in all_seats) and ((seat + 1) not in all_seats)]

if __name__ == "__main__":
    boarding_passes = from_file("input/day_05.txt")
    part_01 = calculate_max_id(boarding_passes)
    print("part_01:-", part_01)

    [part_02] = list(my_seat(boarding_passes))
    print("part_02:-", part_02)
