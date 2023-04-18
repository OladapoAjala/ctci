# ASSUMPTIONS
# 1. Input string has sufficient space at the end to hold additional characters.
# 2. "True" lenght of input string is given

def brute_force(input_str: str, true_len: int) -> str:
    """
    Time: O(n), n true lenght of input string
    Space: O(1)
    """
    if input_str == "":
        return ""
    if input_str == " ":
        return "%20"
    
    alt_char = '%20'
    input_str = input_str[:true_len]
    for i, val in enumerate(input_str):
        if i == true_len:
            break
        if val == " ":
            str_a = input_str[:i]
            str_b = input_str[i+1:]
            input_str = str_a + alt_char + str_b
    return input_str

def simple_pythonic_solution(input_str: str, true_len: int) -> str:
    if input_str == "":
        return ""
    if input_str == " ":
        return "%20"

    input_str = input_str.split()
    return "%20".join(input_str)