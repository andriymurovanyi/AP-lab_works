import numpy as np
shape = input('Размерность: ').split('x')
n = int(shape[0])
m = int(shape[1])
a = b = np.zeros((n, m), int)
for i in range(n):
    for j in range(m):
        a[i, j] = int(input('a[' + str(i) +
                            '][' + str(j) + '] = '))
print(a)
for i in range(n):
    for j in range(m):
        b[i, j] = int(input('b[' + str(i) +
                            '][' + str(j) + '] = '))
print(b)
mult = np.zeros((n, m), int)
for i in range(n):
    for j in range(m):
        for k in range(n):
            mult[i][j] += a[i][k] * b[k][j]
print('Результирующий массив:\n {}'.format(mult))








