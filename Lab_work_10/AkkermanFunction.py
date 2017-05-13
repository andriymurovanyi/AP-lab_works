# Мурованый Андрей. КНИТ16-А
# Условие: Вычислить функцию Аккермана.
import sys


def Akkerman(n, m):
    """
    Функция Аккермана.
    
    Рекурсивный вариант
    :param n: Целое число n
    :param m: Целое число m 
    :return: значение функции Аккермана
    """
    i = 0
    if n == 0:
        i += 100
        return m + 1
    elif n > 0 and m == 0:
        i += 100
        return Akkerman(n - 1, 1)
    elif n > 0 and m > 0:
        i += 100
        return Akkerman(n - 1, Akkerman(n, m - 1))
    return i


def Akkerman_iter(n, m):
    """
    Функция Аккермана.

    Итерационный вариант
    :param n: Целое число n
    :param m: Целое число m 
    :return: значение функции Аккермана
    """
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
    i = 1001
    try:
        i += 100
        sys.setrecursionlimit(i)
    except RecursionError:
        i -= 100
        print('Глубина рекурсии переустановлена в: ', sys.getrecursionlimit())
    n = int(input('n = '))
    m = int(input('m = '))
    ask = input('<1 - Рекурсивно>\n'
                '<2 - Итерационно>\n'
                '>>> ')
    if ask == '1':
        print('Значение функции: ', Akkerman(n, m))
    elif ask == '2':
        print('Значение функции: {}'.format(Akkerman_iter(n, m)))
        i = 1001
        try:
            i += 100
            sys.setrecursionlimit(i)
        except RecursionError:
            i -= 100
            print('Глубина рекурсии переустановлена в: ', sys.getrecursionlimit())
    if input('Press Enter to continue...') != '':
        break


