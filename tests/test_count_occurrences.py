import hw1
import pytest

def test_positive_have_elem():
    lst = [1, 2, 3, 4, 2]
    value = 2
    expected = 2
    result = hw1.count_occurrences(lst, value)

    assert result == expected, f"expected:{expected}, result: {result}"