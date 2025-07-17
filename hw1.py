def find_substr(text:str, pattern:str) -> int:
  """
  Если подстроки нет в строке, ошибка.

  :param text: строка
  :param pattern: часть этой строки
  :return: индекс вхождения pattern в text, или ошибка
  """

  if pattern not in text:
    raise ValueError("pattern not in text(")
  # не понимаю как не через find((
  return text.find(pattern)


def find_elem(lst: list, value: (int, float)) -> int:
  """
  возвращает индекс первого вхождения элемента в список,
  если такого нет, ошибка

  :param lst: список элементов
  :param value: значение
  :return: индекс
  """

  if not isinstance(lst, list):
    raise TypeError("why not list((")

  for i in range(len(lst)):
    if lst[i] == value:
      return i

  raise ValueError("value not in lst((")

def count_occurrences(lst: list, value: (int, float)) -> int:

  """
  ищет количество вхождений value в lst

  :param lst: список элементов
  :param value: искомое значение
  :return: количество или ошибка
  """

  if not isinstance(lst, list):
    raise TypeError("why not list((")

  count = 0
  for i in range(len(lst)):
    if lst[i] == value:
      count += 1

  return count

def reverse_words(s: str) -> str:

  """
  меняет порядок слов в строке на обратный
  :param s:непустая строка
  :return:слова этой строки в обратном порядке
  """

  if len(s) == 0: raise ValueError
  if not isinstance(s, str):
    raise TypeError

  s = s.split(" ")
  new_s = ""

  for i in range(len(s)-1, -1, -1):
    new_s += s[i]
    new_s += " "

  return new_s[:-1:]

def is_palindrome(s: str) -> bool:
  
  ...