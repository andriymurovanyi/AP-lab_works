import numpy as np
n = int(input('Размерность: '))
a = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        a[i, j] = int(input('a[' + str(i) +
                            '][' + str(j) + '] = '))
i = 0
n -= 1
for j in range(n):
    a[i + j][n], a[n][n - j], a[n - j][i], a[i][j] = \
        a[i][j], a[i + j][n], a[n][n - j], a[n - j][i]
print(a)
