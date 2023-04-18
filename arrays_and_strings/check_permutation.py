# ASSUMPTIONS
# 1. Strings aren't sorted.
# 2. Extended ASCII is used for character encoding, max of 256 possible unique characters.
# 3. Case sensitive.

def optimized_by_sorting_input_str(str_a: str, str_b: str) -> bool:
    """
    Time: O(n log n)
    Space: O(1)
    """
    if len(str_a) != len(str_b):
        return False
    
    if str_a == "" and str_b == "":
        return True

    if str_a == str_b:
        return True

    str_a = sorted(str_a)
    str_b = sorted(str_b)

    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            return False

    return True

def optimized_using_hash_map(str_a: str, str_b: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    if len(str_a) != len(str_b):
        return False
    
    if str_a == "" and str_b == "":
        return True

    if str_a == str_b:
        return True   

    str_a_char_count = counter(str_a)
    str_b_char_count = counter(str_b)

    return str_a_char_count == str_b_char_count
    

def counter(input: str) -> dict:
    """
    Time: O(n)
    Space: O(1)
    """
    char_count = {}
    for char in input:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count    