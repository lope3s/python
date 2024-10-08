def vowel_matcher(str_input: str) -> bool:
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    different_vowels = 0

    for vowel in vowel_list:
        if vowel in str_input:
            different_vowels += str_input.count(vowel)

        if different_vowels >= 3:
            return True
        
    return False

def twin_letter_matcher(str_input: str) -> bool:
    input_len = len(str_input)
    for i in range(input_len):
        if i + 1 < input_len:
            letter = str_input[i]
            next_letter = str_input[i + 1]
            if letter == next_letter:
                return True
    return False

def forbidden_matcher(str_input: str) -> bool:
    forbidden_strs = ['ab', 'cd', 'pq', 'xy']

    for forbidden_str in forbidden_strs:
        if forbidden_str in str_input:
            return True
        
    return False

def string_matcher(str_input: str) -> bool:
    has_at_leat_three_different_vowels = vowel_matcher(str_input)
    has_twin_letter = twin_letter_matcher(str_input)
    has_forbidden = forbidden_matcher(str_input)

    if (has_at_leat_three_different_vowels and 
        has_twin_letter and not 
        has_forbidden):
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
