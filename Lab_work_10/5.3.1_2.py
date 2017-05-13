import numpy as np
# Мурованый Андрей. КНИТ16-А
# Условие: написать программу, которая будет содержать функции вычисления:
# * суммы элементов квадратной матрицы;
# * произведения элементов квадратной матрицы;
# * Поиск элемента с заданным значением в квадратной матрице;


def summa_iter(arr):
    """
    Сумма элементов матрицы.
    
    Итерационный вариант
    :param arr: Принимает двумерный массив
    :return: Сумма элементов массива
    """
    s = 0
    for i in arr:
        for j in i:
            s += j
    return s


def summa_rec(arr):
    """
    Сумма элементов матрицы.

    Рекурсивный вариант
    :param arr: Принимает двумерный массив
    :return: Сумма элементов массива
    """
    arr = np.array([i for i in arr.flat], dtype=int)
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + summa_rec(arr[1:])


def mult_iter(arr):
    """
    Произведение элементов матрицы.

    Итерационный вариант
    :param arr: Принимает двумерный массив
    :return: Произведение элементов массива
    """
    m = 1
    for i in arr:
        for j in i:
            m *= j
    return m


def mult_rec(arr):
    """
    Произведение элементов матрицы.

    Рекурсивный вариант
    :param arr: Принимает двумерный массив
    :return: Произведение элементов массива
    """
    arr = np.array([i for i in arr.flat], dtype=int)
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] * mult_rec(arr[1:])


def search_iter(arr, x, ):
    """
    Поиск элемента в матрице.

    Поиск элемента с заданным значением в квадратной матрице
    Итерационный вариант
    :param arr: Принимает двумерный массив
    :param x: Искомый элемент
    :return: Позицию элемента в матрице
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == x:
                return i, j
    else:
        return


def search_rec(arr, x, r, c):
    """
    Поиск элемента в матрице.

    Поиск элемента с заданным значением в квадратной матрице
    Итерационный вариант
    :param c: Индекс для столбца
    :param r: Индекс для строки
    :param arr: Принимает двумерный массив
    :param x: Искомый элемент
    :return: Позицию элемента в матрице
    """
    if arr[r][c] == x:
        return r, c
    else:
        return search_rec(arr, x, r + 1, c + 1)


while True:
    shape = input('Размерность...? \n'
                  '>>> ').split('x')
    n, m = int(shape[0]), int(shape[1])
    arr = np.zeros((n, m), dtype=int)
    for i in range(n):
        for j in range(m):
            arr[i][j] = int(input('A[' + str(i) + '][' + str(j) + '] = '))

    print('Это ваш массив ?\n{}'.format(arr))

    ask = input('Что будем делать ?\n'
                '<1 - Сумма элементов>\n'
                '<2 - Произведение элементов>\n'
                '<3 - Искать элемент в массиве>\n'
                '>>> ')
    if ask == '1':
        ask2 = input('<1 - Рекурсивно>\n'
                     '<2 - Итерационно>\n'
                     '>>> ')
        if ask2 == '1':
            print('Сумма элементов: {}'.format(summa_rec(arr)))
        elif ask2 == '2':
            print('Сумма элементов: {}'.format(summa_iter(arr)))
        else:
            print('Error!')
            continue
    elif ask == '2':
        ask2 = input('<1 - Рекурсивно>\n'
                     '<2 - Итерационно>\n'
                     '>>> ')
        if ask2 == '1':
            print('Произведение элементов: {}'.format(mult_rec(arr)))
        elif ask2 == '2':
            print('Произведение элементов: {}'.format(mult_iter(arr)))
        else:
            print('Error!')
            continue
    elif ask == '3':
        x = int(input('Искомый элемент ... ?: '))
        ask2 = input('<1 - Рекурсивно>\n'
                     '<2 - Итерационно>\n'
                     '>>> ')
        if ask2 == '1':
            print('Элемент находится в {} позиции'.format(search_rec(arr, x, 0, 0)))
        elif ask2 == '2':
            print('Элемент находится в {} позиции'.format(search_iter(arr, x)))
        else:
            print('Error!')
            continue

        print('Oop\'s, you have an Error! ')
    if input('Press Enter to continue...') != '':
        break
