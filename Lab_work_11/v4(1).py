# Мурованый Андрей.КНИТ16-А
# Последовательносто образована по закону x[i] = i - 0.1 / i ** 3 + abs(tan(2*i))
# Вывести в файл значение, для которого выполнилось abs(x[i]) < e
from os import mkdir, getcwd, chdir
from math import tan

chdir('D:/NewFold/MyFold')
print('Мы находимся в следующуей директории:', getcwd())
while True:
    e = float(input('e = '))
    x = [i for i in range(1, 101)]
    for i in range(1, 100):
        x[i] = i - 0.1 / i ** 3 + abs(tan(2*i))
        if abs(x[i]) < e:
            with open('h.txt', 'w') as h:
                h.writelines(str(x[i]))
        else:
            break
    with open('h.txt', 'r') as f:
        line = f.readlines()
    for i in line:
        print(i)

    if input('Press Enter to continue...') != '':
        flag = False
        break
