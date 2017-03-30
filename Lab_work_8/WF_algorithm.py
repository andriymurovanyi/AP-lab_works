from timeit import timeit
setup = '''
haystack = input('Введите строку, в которой искать: ')
needle = input('Искомый шаблон: ')
m = len(haystack)
n = len(needle)
d = [[0 for i in range(n + 1)] for j in range(m + 1)]
'''
stmt = '''
for i in range(m + 1):
    d[i][0] = i
for j in range(n + 1):
    d[0][j] = j
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if haystack[i - 1] == needle[j - 1]:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = 1 + min(d[i - 1][j], d[i - 1][j - 1], d[i][j - 1])
print(d[m][n])
'''
print('Время записи: {} секунд'.format(timeit(stmt, setup, number=1)))
