while True:
    import timeit
    import numpy as np
    n = int(input('Кол-во элементов в массиве: '))
    a = np.arange(N + 1)
    x = int(input('Искомый элемент: '))
    i = 0
    a[n] = x
    while a[i] != x:
        i += 1
    if i == n:
        print('Элемент не найден!')
    else:
        print('Елемент {} найден в {} позиции'.format(x, i))
    if input('Press Enter to continue...') != '':
        break


