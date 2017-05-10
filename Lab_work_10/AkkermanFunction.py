def Akkerman(n, m):
    if n == 0:
        return m + 1
    elif n > 0 and m == 0:
        return Akkerman(n - 1, 1)
    elif n > 0 and m > 0:
        return Akkerman(n - 1, Akkerman(n, m - 1))


def Akkerman_iter(n, m):
    stack = []
    while True:
        if m == 0:
            n += 1
            if not stack:
                return n
            m = stack.pop()
        elif n == 0:
            m -= 1
            n += 1
        else:
            stack.append(m - 1)
            n -= 1


while True:
    try:
        n = int(input('n = '))
        m = int(input('m = '))
        ask = input('<1 - Рекурсивно>\n'
                    '<2 - Итерационно>\n'
                    '>>> ')
        if ask == '1':
            print('Значение функции: ', Akkerman(n, m))
        elif ask == '2':
            print('Значение функции: ', Akkerman_iter(n, m))
    except(ValueError, IndexError, RecursionError):
        print('Проверьте ввод!\n'
              'p.s: Не вводите слишком большие значения')
        continue
    if input('Press Enter to continue...') != '':
        break


