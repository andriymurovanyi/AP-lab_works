def func(c):
    k = 0
    a = c - 1
    while a > c // 2:
        b = c - a
        k += 1 + func(b)
        a -= 1
    return k


def func_iter(c):
    a = c - 1
    return len(list(enumerate(range(a, c // 2 - (c - a), -1))))

while True:
    try:
        c = int(input('Введите число: '))
        ask = input('<1 - Рекурсивно>\n'
                    '<2 - Итерационно>\n'
                    '>>> ')
        if ask == '1':
            print('Количество представлений', func(c))
        elif ask == '2':
            print('Количество представлений', func_iter(c))
    except(ValueError, MemoryError, RecursionError, IndexError):
        print('Ой, ошибка!')
    if input('Press Enter to continue...') != '':
        break

