import time
haystack = input('Строка, в которой ищем: ')
needle = input('Шаблон поиска: ')
d = [0] * len(needle) # Таблица для префикс функции.
j = 0  # Индекс для подстроки(needle).
for i in range(1, len(needle)):
    while j > 0 and needle[i] != needle[j]:
        j = d[j - 1]
        print(d[j - 1])
    if needle[i] == needle[j]:
        j += 1
    d[i] = j
for i in range(0, len(haystack)):
    while j > 0 and needle[j] != haystack[i]:
        j = d[j - 1]
    if needle[j] == haystack[i]:
        j += 1
    if j == len(needle):
        print('Подстрока \'{}\' встречаеться {} позиции'.format(needle, i - j + 1))
        j = d[j - 1]
