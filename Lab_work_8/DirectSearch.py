from timeit import timeit
setup = '''
haystack = input('Введите строку, в которой искать: ')
needle = input('Введите шаблон поиска: ')
a = len(haystack)  # Длина строки, в которой ищем.
b = len(needle)  # Длина шаблона.
i = 0  # Индекс символа строки.
j = 0  # Индекс символа шаблона.
'''
stmt = '''
while i <= a - b and j < b:
    if haystack[i + j] == needle[j]:  # Если буквы совпали - двигаемся по обеим строкам.
        j += 1
    else:
        i += 1
        j = 0  # Откат назад. Ищем с 0-й позиции "needle".
if j == b:
    print('Элемент \\'{}\\' найден в позиции {}!'.format(needle, i + 1))
else:
    print('Элемента в строке нет!')
    '''
print('Время записи: {} секунд'.format(timeit(stmt, setup, number=1)))

