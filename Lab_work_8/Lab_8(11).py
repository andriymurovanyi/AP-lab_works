import numpy as np
while True:
    print('Выберите, что хотите сделать: ')
    ans = input('[1 - Повернуть массив]\n'
                '[2 - Циклически сдвинуть]\n'
                '[3 - Выполнить произведение матриц]\n'
                '[4 - Вычислить определитель]\nЯ:')
    # Поворот на 90 градусов.
    if ans == '1':
        try:
            shape = input('Введите размерность:').split('x')
            n = m = int(shape[0])
            a = np.zeros((n, m), dtype=int)
        except (IndexError, ValueError):
            print('Введите размерность корректно!')
        else:
            for i in range(n):
                for j in range(m):
                    a[i, j] = int(input('a[' + str(i) + ']'
                                        '[' + str(j) + '] = '))
            print(np.rot90(a, 3), sep='\t')
    # Сдвиг на К елементов.
    elif ans == '2':
        lenght = int(input('Введите длинну массива: '))
        b = np.zeros(lenght, dtype=int)
        for i in range(lenght):
            b[i] = int(input('b[' + str(i) + '] = '))
        k = int(input('На сколько позиций сдвинуть? \n'))
        print('Результат {}'.format(np.roll(b, -k)))
    # Произведение двух матриц.
    elif ans == '3':
        m = n = int(input('Введите размерность:'))
        a = b = np.zeros((n, m), dtype=int)
        for i in range(n):
            for j in range(m):
                a[i, j] = a[i, j] = int(input('a[' + str(i) +
                                              '][' + str(j) + '] = '))
                print('Mатрица 1: \n', a)
                b[i, j] = a[i, j] = int(input('b[' + str(i) +
                                              '][' + str(j) + '] = '))
                print('Матрица 2: \n', b)
        print(np.matrix(np.dot(np.matrix(a), np.matrix(b))))
    # Определитель матрицы.
    elif ans == '4':
        n = m = int(input('Размерность: '))
        a = np.zeros((n, m), dtype=int)
        for i in range(n):
            for j in range(m):
                a[i, j] = int(input('a[' + str(i) + '][' + str(j) + '] = '))
        print('Определитель{}'.format(np.linalg.det(a)))




