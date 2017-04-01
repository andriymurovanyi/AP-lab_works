import numpy as np


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp


def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return det2(matrix)

    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))

n = int(input('Размерность: '))
a = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        a[i, j] = int(input('a[' + str(i) +
                            '][' + str(j) + '] = '))

print(a)

print('Детерминант матрицы: ', determinant(a))
