import re

def characters_in_code(input: str) -> int:
    return len(input.strip())

def characters_in_memory(input: str) -> int:
    striped_input = input.strip()
    inmemory_str = striped_input[1:len(striped_input) - 1]
    character_in_memory_raw = len(inmemory_str)
    single_backslashes = inmemory_str.count('\\\\')
    single_double_quotes = inmemory_str.count('\\"')
    hexadecimal_representations = len(
        re.findall(r'\\x[a-fA-F0-9]{2}', inmemory_str)
    )
    return (character_in_memory_raw - 
            single_backslashes - 
            single_double_quotes - 
            (hexadecimal_representations * 4) + 
            hexadecimal_representations)

def count_file(file: str) -> None:
    with open(file) as f:
        number_character_in_code = 0
        number_character_in_memory = 0

        for line in f:
            number_character_in_code += characters_in_code(line)
            number_character_in_memory += characters_in_memory(line)

        print(
            number_character_in_code - number_character_in_memory
        )

def encode_code_characters(input: str) -> int:
    # What we really want to count are the number of backslashes and
    # double quotes as those are really, the only ones that we'll be
    # scapping.
    striped_input = input.strip()
    character_in_memory_raw = len(striped_input)
    single_double_quotes = striped_input[1:character_in_memory_raw - 1].count('"')
    single_backslashes = striped_input.count('\\')
    return (character_in_memory_raw + 
            single_backslashes + 
            single_double_quotes +
            4) # padding added to begining and ending of each line (\"\")


def count_encode_file(file: str) -> None:
    with open(file) as f:
        number_character_in_code = 0
        number_character_in_encoded = 0

        for line in f:
            number_character_in_code += characters_in_code(line)
            number_character_in_encoded += encode_code_characters(line)

        print(
            number_character_in_encoded - number_character_in_code
        )

if __name__ == "__main__":
    count_file("input.txt")
    count_encode_file("input.txt")
