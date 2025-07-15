def find_substr(text:str, pattern:str) -> int:
  """
  Если подстроки нет в строке, ошибка.

  :param text: строка
  :param pattern: часть этой строки
  :return: индекс вхождения pattern в text, или ошибка
  """

  if pattern not in text:
    raise ValueError("pattern not in text(")

  return text.find(pattern)


def find_elem(lst: list, value: (int, float)) -> int:
  """
  возвращает индекс первого вхождения элемента в список,
  если такого нет, ошибка

  :param lst: список элементов
  :param value: значение
  :return: индекс
  """

  if value not in lst:
    raise ValueError("value not in lst((")

  if not isinstance(lst, list):
    raise TypeError("why not list((")

  return lst.index(value)

def count_occurrences(lst: list, value: (int, float)) -> int:
  """
  ищет количество вхождений value в lst

  :param lst: список элементов
  :param value: искомое значение
  :return: количество или ошибка
  """
  if not isinstance(lst, list):
    raise TypeError("why not list((")

  return lst.count(value)

def reverse_words(s: str) -> str:
  ...

def is_palindrome(s: str) -> bool:
  ...