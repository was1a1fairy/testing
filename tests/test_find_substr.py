import hw1


def positive_one_entry():
    text = "мне лень придумывать что писать"
    pattern = "лень"
    expected = 4

    result = hw1.find_substr(text, pattern)
    assert result == expected, f"expected: {expected}, result: {result}."