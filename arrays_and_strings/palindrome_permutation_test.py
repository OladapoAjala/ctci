from palindrome_permutation import (
    brute_force,
    optimized_with_hash_map,
    optimized_by_sorting_input,
)

def test_brute_force():
    result = brute_force("tact coa")
    assert result == True
    result = brute_force("tact coat")
    assert result == False
    result = brute_force("Touris rsiout")
    assert result == True

def test_optimized_with_hash_map():
    result = optimized_with_hash_map("tact coa")
    assert result == True
    result = optimized_with_hash_map("tact coat")
    assert result == False
    result = optimized_with_hash_map("Touris rsiout")
    assert result == True

def test_optimized_by_sorting_input():
    result = optimized_by_sorting_input("tact coa")
    assert result == True
    result = optimized_by_sorting_input("tact coat")
    assert result == False
    result = optimized_by_sorting_input("Touris rsiout")
    assert result == True