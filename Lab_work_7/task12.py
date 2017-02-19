# Murovanyi Andriy, KNIT16-А
# Написать программу вычисления суммы тех элементов матрицы а,
# номера строк и столбцов которых принадлежат соответсвенно
# непустым множествам s_1 и s_2.

n = 10
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
s_1 = {i for i in range(n)}
s_2 = {i for i in range(n)}
s = 0
for i in range(len(a)):
    for j in range(len(a)):
        if i in s_1 and j in s_2:
            s += a[i][j]
print('Summa: {}'.format(s))
