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
            n = int(shape[0])
            m = int(shape[1])
            a = np.zeros((n, m), dtype=int)
        except (IndexError, ValueError):
            print('Введите размерность корректно!')
        else:
            if not m == n:
                print('Матрица должна быть квадратной!')
            else:
                for i in range(n):
                    for j in range(m):
                        a[i, j] = int(input('a[' + str(i) + '][' + str(j) + '] = '))
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
        print('Введите размерность!')
        b = np.matrix(np.zeros((int(input()), int(input()))), dtype=int)

        print(b)
        pass
    # Определитель матрицы.
    elif ans == '4':
        n = m = int(input('Размерность: '))
        a = np.zeros((n, m), dtype=int)
        for i in range(n):
            for j in range(m):
                a[i, j] = int(input('a[' + str(i) + '][' + str(j) + '] = '))
        print('Определитель{}'.format(np.linalg.det(a)))




