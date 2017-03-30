from timeit import timeit
setup = '''
haystack = input('Введите строку, в которой искать: ')
needle = input('Искомый шаблон: ')
n = len(haystack)
m = len(needle)
if m > n:
    print('Шаблона нет в строке!')
    '''
stmt = '''
skip = []
for k in range(256):
    skip.append(m)
for k in range(m-1):
    skip[ord(needle[k])] = m - k - 1
skip = tuple(skip)
k = m - 1
while k < n:
    j = m - 1
    i = k
    while j >= 0 and haystack[i] == needle[j]:
        j -= 1
        i -= 1
    if j == -1:
        print('Элемент найден в {} позиции'.format(i + 1))
    else:
        print('Ничего не найдено!')
    k += skip[ord(haystack[k])]
    '''
print('Время записи: {} секунд'.format(timeit(stmt, setup, number=1)))
