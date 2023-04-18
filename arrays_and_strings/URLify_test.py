from URLify import (
    brute_force,
    simple_pythonic_solution,
)

def test_brute_force():
    result = brute_force("", 0)
    assert result == ""
    result = brute_force(" ", 1)
    assert result == "%20"
    result = brute_force("Hello World ", 11)
    assert result == "Hello%20World"

def test_simple_pythonic_solution():
    result = simple_pythonic_solution("", 0)
    assert result == ""
    result = simple_pythonic_solution(" ", 1)
    assert result == "%20"
    result = simple_pythonic_solution("Hello World ", 11)
    assert result == "Hello%20World"   