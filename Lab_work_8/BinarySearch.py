import numpy as np
c = True
while c:
    n = int(input('Кол-во элементов в массиве: '))
    a = np.arange(n + 1)
    x = int(input('Искомый элемент: '))
    right = len(a) - 1
    left = 0
    div = 0
    flag = False
    while left <= right and not flag:
        div = int(left + right) * 5 // 8  # Разделение массива по "Золотому сечению"
        # Уменьшаем зону поиска.
        if a[div] < x:
            left = div + 1
        elif a[div] > x:
            right = div - 1
        else:
            flag = True  # Элемент найден.
    if flag:
        print('Елемент {} найден в {} позиции'.format(x, div))
    else:
        print('Элемента нету в массиве!')

    if input('Press Enter to continue...') != '':
        c = False






