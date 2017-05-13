# Мурованый Андрей. КНИТ16-А
# Условие задачи: Даны натуральные числа (n, m), найти найбольший общий делитель.


def rec(n, m):
    """
    Найбольший общий делитель. Рекурсивно
    
    :param n: Целое число n
    :param m: Целое число m
    :return: Найбольший общий делитель
    """
    if m == 0:
        return n
    else:
        return nod(m, n % m)


def iter(n, m):
    """
    Найбольший общий делитель. Итерационное

    :param n: Целое число n
    :param m: Целое число m
    :return: Найбольший общий делитель
    """
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
    for i in range(n):
        x[i] = int(input('x[{}]: '.format(i + 1)))
    print(x)
    for i in x:
        x[i] = i - 0.1 / i ** 3 + abs(tan(2*i))
        if abs(x[i]) < e:
            with open('h.txt', 'w') as h:
                h.write(str(x[i]))
        else:
            break