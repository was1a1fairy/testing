import hw1
import pytest


def test_positive_upper_register():
    s = "Довод"
    expected = True
    result = hw1.is_palindrome(s)

    assert expected == result, f"{expected}, {result}"


def test_positive_with_space():
    s = "то по р ропот "
    expected = True
    result = hw1.is_palindrome(s)

    assert expected == result, f"{expected}, {result}"


def test_positive_not_palindrome():
    s = "мяу"
    expected = False
    result = hw1.is_palindrome(s)

    assert result == expected, f"{expected}, {result}"


def test_another_type():
    with pytest.raises(TypeError):
        hw1.is_palindrome(12345)