import string, random
from is_unique import (
    brute_force,
    optimized_with_hash_map,
    optimized_by_sorting_input_str,
)

test_data_132 = "6JNu9Kvn8zhoWtyqV4OgPrLsUQ7wCfjZlYc51TbRXdaiSIm0MmxpkHcbdme23Iatr6Fw98JKQZVzHgLfv0jNuWtyqo5NcPrsUQv7wCfjZlYh51TbRXdaiSIm0MmxpkHcbdme"


def generate_string(length):
    return "".join(random.sample(string.ascii_letters + string.digits, length))


def test_brute_force():
    result = brute_force("")
    assert result == False
    result = brute_force("dapo")
    assert result == True
    result = brute_force(generate_string(62))
    assert result == True
    result = brute_force(test_data_132)
    assert result == False


def test_optimized_with_hash_map():
    result = optimized_with_hash_map("")
    assert result == False
    result = optimized_with_hash_map("dapo")
    assert result == True
    result = optimized_with_hash_map("dapao")
    assert result == False
    result = brute_force(generate_string(62))
    assert result == True
    result = brute_force(test_data_132)
    assert result == False


def test_optimized_by_sorting_input_str():
    result = optimized_by_sorting_input_str("")
    assert result == False
    result = optimized_by_sorting_input_str("dapo")
    assert result == True
    result = optimized_by_sorting_input_str("dapao")
    assert result == False
    result = brute_force(generate_string(62))
    assert result == True
    result = brute_force(test_data_132)
    assert result == False
