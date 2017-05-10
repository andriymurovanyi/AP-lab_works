def rec(n, m):
    if m == 0:
        return n
    else:
        return nod(m, n % m)


def iter(n, m):
    while m:
        n, m = m, n % m
    return a


while True:
    try:
        n, m = int(input('n = ')), int(input('m = '))
    except(ValueError, MemoryError):
        print('Что-то пошло не так...')
        continue
    else:
        x = input('[1] - Рекурсия или [2] - Итерация ?')
        if x == '1':
            print('НОД =', rec(n, m))
        elif x == '2':
            print('НОД =', iter(a, b))
        else:
            print('Такого варианта тут нет!')
            continue
    if input('Press Enter to continue...') != '':
        break
