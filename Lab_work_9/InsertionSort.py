import numpy as np


def insertion_sort(mass):
    a = mass
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j - 1] > v) and (j > 0):
            a[j] = a[j - 1]
            j -= 1
        a[j] = v
    return a


mass = np.array(input('Введите массив для сортировки: ').split(', '), dtype=int)
print(insertion_sort(mass))
