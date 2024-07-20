from re import match, findall
from typing import TypedDict

def init_grid_bool() -> list[list[bool]]:
    return [[False for _ in range(1000)] for _ in range(1000)]

def init_grid_int() -> list[list[int]]:
    return [[0 for _ in range(1000)] for _ in range (1000)]

InstructionDict = TypedDict(
    "InstructionDict",
    {
        'instruction': str,
        'range_start': tuple[int, int],
        'range_end': tuple[int, int]
    }
)

def instruction_parser(str_input: str) -> InstructionDict:
    ranges: list[str] = findall(r'[0-9,]+', str_input)
    instruction = match(r'^[^0-9,]+', str_input)

    instruction_dict: InstructionDict = {
        'instruction': '',
        "range_start": (0,0),
        "range_end": (0,0)
    }

    if instruction != None:
        instruction_dict["instruction"] = instruction[0].strip()

    start_ranges = ranges[0].split(',')
    instruction_dict["range_start"] = (int(start_ranges[0]), int(start_ranges[1]))

    end_ranges = ranges[1].split(',')
    instruction_dict["range_end"] = (int(end_ranges[0]), int(end_ranges[1]))

    return instruction_dict

def count_lights_bool(grid: list[list[bool]]) -> int:
    count = 0
    for row in grid:
        for col in row:
            if col:
                count += 1

    return count

def count_lights_int(grid: list[list[int]]) -> int:
    count = 0
    for row in grid:
        for col in row:
                count += col

    return count

def switcher_controller_bool(grid: list[list[bool]], instruction: InstructionDict) -> None:
    range_start = instruction["range_start"]
    range_end = instruction["range_end"]
    command = instruction["instruction"]

    for i in range(range_start[0], range_end[0] + 1):
        for j in range(range_start[1], range_end[1] + 1):
            if command == "turn on":
                grid[i][j] = True
            elif command == "turn off":
                grid[i][j] = False
            else:
                curr = grid[i][j]
                grid[i][j] = not curr

def switcher_controller_int(grid: list[list[int]], instruction: InstructionDict) -> None:
    range_start = instruction["range_start"]
    range_end = instruction["range_end"]
    command = instruction["instruction"]

    for i in range(range_start[0], range_end[0] + 1):
        for j in range(range_start[1], range_end[1] + 1):
            if command == "turn on":
                grid[i][j] += 1
            if command == "turn off" and grid[i][j] > 0:
                grid[i][j] -= 1
            if command == 'toggle':
                grid[i][j] += 2

if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()
        grid = init_grid_int()

        while line:
            instructions = instruction_parser(line)
            switcher_controller_int(grid, instructions)
            line = f.readline().strip()

        lights_on = count_lights_int(grid)
        print(f'There where {lights_on} lights on at the end of the instructions')

        
