from check_permutation import (
    optimized_by_sorting_input_str,
    optimized_using_hash_map
)

def test_optimized_by_sorting_input_str():
    result = optimized_by_sorting_input_str("", "")
    assert result == True
    result = optimized_by_sorting_input_str("abcd", "ab")
    assert result == False  
    result = optimized_by_sorting_input_str("abcd", "abcd")
    assert result == True
    result = optimized_by_sorting_input_str("lkmshtis", "mkltihss")
    assert result == True
    result = optimized_by_sorting_input_str("lkmshtiis", "mkltijhss")
    assert result == False

def test_optimized_using_hash_map():
    result = optimized_using_hash_map("", "")
    assert result == True
    result = optimized_using_hash_map("abcd", "ab")
    assert result == False  
    result = optimized_using_hash_map("abcd", "abcd")
    assert result == True
    result = optimized_using_hash_map("lkmshtis", "mkltihss")
    assert result == True
    result = optimized_using_hash_map("lkmshtiis", "mkltijhss")
    assert result == False