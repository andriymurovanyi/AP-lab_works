
from timeit import timeit
setup = '''
import numpy as np
n = int(input('Кол-во элементов в массиве: '))
a = np.arange(n + 1)
x = int(input('Искомый элемент: '))
right = len(a) - 1  # Правая граница.
left = 0  # Левая граница.
div = 0
'''
stmt = '''
while left <= right:
    div = int(left + right) // 2  # Метод "дихотомии"
    # Уменьшаем зону поиска.
    if x < a[div]:
        right = div - 1
    elif x > a[div]:
        left = div + 1
    else:
        x = div  # Элемент найден!
        break
if x == div:
    print('Елемент {} найден в {} позиции'.format(x, div))
else:
    print('Елемент не найден!')
    '''
print('Время записи: {} секунд'.format(timeit(stmt, setup, number=1)))








