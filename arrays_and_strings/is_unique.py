# Assuming extended ACSII encoded characters -> 256 maximum number of characters

def brute_force(input_str: str) -> bool:
    """
    Time: O(n^2), n <= 256
    Space: O(1)
    """
    if len(input_str) > 256:
        return False 

    if len(input_str) == 0:
        return False

    for i, char in enumerate(input_str):
        start = i+1
        for x_char in input_str[start:]:
            if char == x_char:
                return False
    
    return True

def optimized_with_hash_map(input_str: str) -> bool:
    """
    Time:   O(n), n <= 256
    Space:  O(n), n <= 256

    NOTE: there are 256 possible extended ASCII encoded chars.
    """
    if len(input_str) > 256:
        return False 

    if len(input_str) == 0:
        return False

    hash_map = {}
    for char in input_str:
        hash_map[char] = hash_map.get(char, 0) + 1
    
    for count in hash_map.values():
        if count > 1:
            return False 

    return True

def optimized_by_sorting_input_str(input_str: str) -> bool:
    """
    Time: O(n log n), n <= 256
    Space: O(1)
    """
    if len(input_str) > 256:
        return False 

    if len(input_str) == 0:
        return False

    input_str = sorted(input_str)
    for i in range(0, len(input_str)-1):
        if input_str[i] == input_str[i+1]:
            return False 
    
    return True
