import numpy as np


def selection_sort(mass):
    a = mass
    for i in range(len(a)):
        idxMin = i
        for j in range(i + 1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a


mass = np.array(input('Введите массив для сортировки: ').split(', '), dtype=int)
print(selection_sort(mass))
