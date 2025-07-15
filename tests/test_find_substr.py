import hw1


def positive_one_entry():
    text = "мне лень придумывать что писать"
    pattern = "лень"
    expected = 4

    result = hw1.find_substr(text, pattern)
    assert result == expected, f"expected: {expected}, result: {result}."

def positive_two_entry():
    text = "мне лень придумывать что писать, лень"
    pattern = "лень"
    expected = 4

    result = hw1.find_substr(text, pattern)
    assert result == expected, f"expected: {expected}, result: {result}."
