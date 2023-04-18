"""
ASUMPTIONS:
    1. The words don't have to be a dictionary word.

INSIGHTS:
For a string to be a palindrome, the following much be true:
    1. Every letter must occur an even number of times.
    2. Atmost one letter can occur an odd number of times.

QUESTIONS: 
    1. What of none alphabetic chars?
"""

def brute_force(input_str: str) -> bool:
    """
    Time: O(n^2)
    Space: O(1)
    """
    if len(input_str) == 0:
        return False
    if len(input_str) == 1 or len(input_str) == 2:
        return True 

    odd_count = 0
    for char in input_str:
        if char == ' ':
            continue
        count = 0
        for char_x in input_str:
            if char_x.lower() == char.lower():
                count += 1
        
        if count % 2 != 0:
            odd_count += 1

        if odd_count > 1:
            return False
    
    return True

def optimized_with_hash_map(input_str: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    if len(input_str) == 0:
        return False
    if len(input_str) == 1 or len(input_str) == 2:
        return True 

    store = {}
    for char in input_str:
        if char == ' ':
            continue
        tmp = char.lower()
        store[tmp] = store.get(tmp, 0) + 1

    found_odd = False
    for _, val in store.items():
        if val % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    
    return True

def optimized_by_sorting_input(input_str: str) -> bool:
    """
    Time: O(n log n)
    Space: O(1)
    """
    sorted_input = "".join(sorted(input_str.lower())).strip()
    count = 1
    odd_count = 0
    for i in range(1, len(sorted_input)):
        if sorted_input[i] != sorted_input[i-1]:
            if count % 2 != 0:
                if odd_count != 0:
                    return False 
                odd_count += 1
            count = 1
            continue
        count += 1 

    if count % 2 != 0:
        if odd_count != 0:
            return False
    return True