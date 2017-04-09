import numpy as np


def bubble_sort(mass):
    a = mass
    n = 1
    while n < len(mass):
        for i in range(len(mass) - n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        n += 1
    return a


a = input('Введите элементы для сортировки: ').split(', ')
mass = np.array(a, dtype=int)
print('Отсортированный массив: ', bubble_sort(mass))
