from one_away import (
    one_way,
)

def test_one_way():
    result = one_way("verydifferentstr", "string")
    assert result == False
    result = one_way("pale", "ple")
    assert result == True
    result = one_way("pales", "pale")
    assert result == True
    result = one_way("pale", "bale")
    assert result == True
    result = one_way("pale", "bake")
    assert result == False
    result = one_way("bple", "ple")
    assert result == True