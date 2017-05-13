# Мурованый Андрей. КНИТ16-А.
# Условие: сформировать функцию подсчета количества различных представлений
# заданного натурального числа n в виде суммы не менее двух попарно различных
# натуральных слагаемых.


def rec_decompose(c):
    def func(c, id):
        """
        Функция подсчета представлений числа.
        
        Рекурсивный вариант.
        :param c: Натуральное целое число.
        :return: Количетво разложений числа.
        """
        if c == 0 and id == 0:
            return 1
        if c <= 0 or id <= 0:
            return 0
        return func(c - id, id) + func(c - 1, id - 1)
    stack = []
    if c == 0 or c == 1:
        return 0
    for i in range(1, c):
        stack.append(func(c, i))
    return max(stack)


def func_iter(c):
    """
    Функция подсчета представлений числа.

    Итерационный вариант.
    :param c: Натуральное целое число.
    :return: Количетво разложений числа.
    """
    a = c - 1
    return len(list(enumerate(range(a, c // 2 - (c - a), -1), start=1)))

while True:
    try:
        c = int(input('Введите число: '))
        ask = input('<1 - Рекурсивно>\n'
                    '<2 - Итерационно>\n'
                    '>>> ')
        if ask == '1':
            print('Количество представлений', rec_decompose(c))
        elif ask == '2':
            print('Количество представлений', func_iter(c))

    except(ValueError, MemoryError, RecursionError, IndexError):
        print('Ой, ошибка!')
    if input('Press Enter to continue...') != '':
        break

