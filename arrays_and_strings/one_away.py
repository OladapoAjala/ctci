"""
ASSUMPTIONS:
    1.English alphabets (although, it works fine for any set of characters).
INSIGHTS:
    1. Maximum lenght differences is 1.
    2. Atmost one char can be different/absent.
    3. The order in which the letters occur matter.
"""

def one_way(str_one: str, str_two: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    len_diff = abs(len(str_one) - len(str_two))
    if len_diff > 1:
        return False
    
    i, j = 0, 0
    found_diff = False
    while i < len(str_one) and j < len(str_two):
        if str_one[i] != str_two[j]:
            if found_diff: 
                return False 
            found_diff = True

            if len(str_one) > len(str_two):
                i += 1
                continue
            elif len(str_two) > len(str_one):
                j += 1
                continue

        i += 1
        j += 1
    
    return True