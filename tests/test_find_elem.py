import hw1
import pytest

def test_positive_one_entry():
    lst = [1, 2, 3, 4]
    value = 3
    expected = 2

    result = hw1.find_elem(lst, value)
    assert result == expected, f"expected: {expected}, result: {result}"
