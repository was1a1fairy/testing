import hw1
import pytest


def test_positive_one_entry():
    text = "мне лень придумывать что писать"
    pattern = "лень"
    expected = 4

    result = hw1.find_substr(text, pattern)
    assert result == expected, f"expected: {expected}, result: {result}."

def test_positive_two_entry():
    text = "мне лень придумывать что писать, лень"
    pattern = "лень"
    expected = 4

    result = hw1.find_substr(text, pattern)
    assert result == expected, f"expected: {expected}, result: {result}."

def test_negative_zero_entry():
    text = "мне лень придумывать что писать"
    pattern = "класс"

    with pytest.raises(ValueError):
        hw1.find_substr(text, pattern)