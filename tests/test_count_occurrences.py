import hw1
import pytest


def test_positive_have_elem():
    lst = [1, 2, 3, 4, 2]
    value = 2
    expected = 2
    result = hw1.count_occurrences(lst, value)

    assert result == expected, f"expected:{expected}, result: {result}"


def test_positive_no_elem():
    lst = [1, 2, 3, 4, 2]
    value = 5
    expected = 0
    result = hw1.count_occurrences(lst, value)

    assert result == expected, f"expected:{expected}, result: {result}"


def test_positive_empty():
    lst = []
    value = 5
    expected = 0
    result = hw1.count_occurrences(lst, value)

    assert result == expected, f"expected:{expected}, result: {result}"


def test_negative_not_list():
    lst = "string"
    value = "t"

    with pytest.raises(TypeError):
        hw1.count_occurrences(lst, value)


def test_positive_diff_types():
    lst = [1, "2", 4.44, -5]
    value = 1
    expected = 1
    result = hw1.count_occurrences(lst, value)

    assert result == expected, f"expected:{expected}, result: {result}"