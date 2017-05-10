import numpy as np
from os import mkdir, getcwd, chdir
from math import tan
chdir('D:/NewFold/MyFold')
print('Мы находимся в следующуей директории:', getcwd())
while True:
    e = float(input('e = '))
    n = int(input('Введите кол-во элементов: '))
    x = np.zeros(n, dtype=int)
    for i in range(n):
        x[i] = int(input('x[{}]: '.format(i + 1)))
    for i in x:
        x[i] = i - 0.1 / i ** 3 + abs(tan(2*i))
        if abs(x[i]) < e:
            with open('h.txt', 'w') as h:
                h.write(str(x[i]))
        else:
            break
    with open('h.txt', 'r') as f:
        line = f.readlines()
    for i in line:
        print(i)

    if input('Press Enter to continue...') != '':
        flag = False
        break
