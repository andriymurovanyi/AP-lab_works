import numpy as np
lenght = int(input('Введите длинну массива: '))
k = int(input('На сколько позиций сдвинуть? \nЯ:')) % lenght
b = np.zeros(lenght, dtype=int)
for i in range(lenght):
    b[i] = int(input('b[' + str(i) + '] = '))
i = 0
t = b[i]
for j in range(lenght):
    i -= k
    if i > 0:
        i += lenght
    t, b[i] = b[i], t
print('Результирующий массив: ', b)
