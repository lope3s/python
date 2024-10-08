DEFAULT_INPUT_STR_SIZE = 16

def has_not_overlapping_double_twin_letters(str_input: str) -> bool:
    for i in range(0, DEFAULT_INPUT_STR_SIZE - 2):
        pair = str_input[i:i + 2]
        if str_input.count(pair) >= 2:
            return True
    return False

def has_single_spread_twin_letters(str_input: str) -> bool:
    for i in range(0, DEFAULT_INPUT_STR_SIZE - 2):
        current_letter = str_input[i]
        next_letter = str_input[i + 2]
        if current_letter == next_letter:
            return True
    return False

def string_matcher(str_input: str) -> bool:
    not_overlapping_double_twin_letters = has_not_overlapping_double_twin_letters(str_input)
    single_spread_twin_letter = has_single_spread_twin_letters(str_input)

    if not_overlapping_double_twin_letters and single_spread_twin_letter:
        return True

    return False

if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()
        nice_strs = 0

        while line:
            if string_matcher(line):
                nice_strs += 1
            line = f.readline().strip()

        print(f'There where {nice_strs} nice strings in the input file.')
