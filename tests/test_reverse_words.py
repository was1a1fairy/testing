import pytest

import hw1


def test_three_words():
    s = "лень придумывать строку"
    expected = "строку придумывать лень"
    result = hw1.reverse_words(s)

    assert result == expected, f"{expected}, {result}"

def test_one_word():
    s = "мяу"
    expected = "мяу"
    result = hw1.reverse_words(s)

    assert result == expected, f"{expected}, {result}"

def test_negative_empty():
    with pytest.raises(ValueError):
        hw1.reverse_words("")