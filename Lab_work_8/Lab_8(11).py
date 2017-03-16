import numpy as np


def matrix():  # Инициализируем массив для его дальнейшего использования.
    shape = input('Размерность: ').split('x')
    n = int(shape[0])
    m = int(shape[1])
    global a, b
    a = np.zeros((n, m), dtype=int)
    b = np.zeros((n, m), dtype=int)
    for i in range(n):
        for j in range(m):
            a[i, j] = int(input('a[' + str(i) +
                                '][' + str(j) + '] = '))
            if ans == '3':
                b[i, j] = int(input('b[' + str(i) +
                                    '][' + str(j) + '] = '))
while True:
    print('Выберите, что хотите сделать: ')
    ans = input('[1 - Повернуть массив]\n'
                '[2 - Циклически сдвинуть]\n'
                '[3 - Выполнить произведение матриц]\n'
                '[4 - Вычислить определитель]\nЯ:')
    # Поворот на 90 градусов.
    if ans == '1':
        matrix()
        print('Начальный массив: \n', np.matrix(a))
        print('Результирующий массив:\n', np.rot90(a, -1))
    # Сдвиг на К елементов.
    elif ans == '2':
        lenght = int(input('Введите длинну массива: '))
        b = np.zeros(lenght, dtype=int)
        for i in range(lenght):
            b[i] = int(input('b[' + str(i) + '] = '))
        k = int(input('На сколько позиций сдвинуть? \nЯ:'))
        print('Результат {}'.format(np.roll(b, -k)))
    # Произведение двух матриц.
    elif ans == '3':
        matrix()
        print('Матрица 1:\n', np.matrix(a))
        print('Матрица 2: \n', np.matrix(b))
        print('Вот, что получилось:\n',np.matrix(np.dot(np.matrix(a),
                                                        np.matrix(b))))
    # Определитель матрицы.
    elif ans == '4':
        matrix()
        print('Определитель: {}'.format(int(np.linalg.det(a))))
    if input('Чтобы продолжить нажмите Enter...') != '':
        break
