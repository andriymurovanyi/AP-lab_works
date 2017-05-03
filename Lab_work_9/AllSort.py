import numpy as np
import random as rnd
from time import clock, time



def bubble_sort(arr, h):
    """
    Bubble sort.
    
    Is a simple sorting algorithm that repeatedly steps through
    the list to be sorted, compares each pair of adjacent items
    and swaps them if they are in the wrong order.
    
    Take 2 positional arguments arr, h
    :param h: how you want to sort
    :param arr: array, which need to sort.
    
    :return: sorted sequence arr
    """
    comp = 0
    swap = 0
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            comp += 1
            if h == 1:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swap += 1
            elif h == 2:
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swap += 1
        n += 1
    return arr, comp, swap


def selection_sort(arr, h):
    """
    Selection sort.
    
    Selection sort is a sorting algorithm,
    specifically an in-place comparison sort.
    
    Take 2 positional arguments arr, comp, swap
    :param h: how you want to sort
    :param arr: array, which need to sort.
    
    :return: sorted sequence arr
    """
    comp = 0
    swap = 0
    for i in range(len(arr) - 1):
        comp += 1
        minimum = i
        for j in range(i + 1, len(arr)):
            comp += 2
            if h == 1:
                if arr[j] < arr[minimum]:
                    minimum = j
            elif h == 2:
                if arr[j] > arr[minimum]:
                    minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
        swap += 1
    return arr, comp, swap


def insertion_sort(arr, h):
    """
    Insertion sort.
    
    Insertion sort is a simple sorting algorithm that
    builds the final sorted array (or list) one item
    at a time.
    
    Take 2 positional arguments arr, comp, swap
    :param h: how you want to sort
    :param arr: array, which need to sort.
    
    :return: sorted sequence arr
    """
    comp = 0
    swap = 0
    for i in range(1, len(arr)):
        comp += 2
        if h == 1:
            while i > 0 and arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
                swap += 1
        elif h == 2:
            while i > 0 and arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
                swap += 1
    return arr, comp, swap


def cocktail_sort(arr, h):
    """
    Cocktail sort. 
    
    Is a variation of bubble sort that is both a
    stable sorting algorithm and a comparison sort.
    
    Take 2 positional arguments arr, comp, swap
    :param h: how you want to sort
    :param arr: array, which need to sort.
    
    :return: sorted sequence arr
    """
    comp = 0
    swap = 0
    up = range(len(arr) - 1)
    while True:
        for i in (up, reversed(up)):
            c = False
            for j in i:
                comp += 1
                if h == 1:
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        c = True
                        swap += 1
                elif h == 2:
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        c = True
                        swap += 1
            if not c:
                return arr, comp, swap


def shell_sort(arr, h):
    """
    Shell sort.
    Is an in-place comparison sort
    
    Take 2 positional arguments arr, comp, swap
    :param h: how you want to sort
    :param arr: array, which need to sort.
    
    :return: sorted sequence arr
    """
    comp = 0
    swap = 0
    div = len(arr) // 2
    while div:
        for i, el in enumerate(arr):
            comp += 1
            if h == 1:
                while i >= div and arr[i - div] > el:
                    arr[i] = arr[i - div]
                    i -= div
                    swap += 1
            elif h == 2:
                while i >= div and arr[i - div] < el:
                    arr[i] = arr[i - div]
                    i -= div
                    swap += 1
            arr[i] = el
        div = 1 if div == 2 else div * 5 // 8
    return arr, comp, swap


def heapify(arr, n, i, h):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    # See if left child of root exists and is
    # greater than root
    if h == 1:
        if l < n and arr[i] < arr[l]:
            largest = l
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
    elif h == 2:
        if l < n and arr[i] > arr[l]:
            largest = l
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] > arr[r]:
            largest = r
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest, h)


# The main function to sort an array of given size
def heap_sort(arr, h):
    """
    Heap sort.
    
    Heapsort is a comparison-based sorting algorithm. Heapsort can be
    thought of as an improved selection sort: like that algorithm, it
    divides its input into a sorted and an unsorted region, and it 
    iteratively shrinks the unsorted region by extracting the largest 
    element and moving that to the sorted region.

    Take 2 positional arguments arr, comp, swap
    :param h: how you want to sort
    :param arr: array, which need to sort.
    
    :return: sorted sequence arr
    """
    comp = 0
    swap = 0
    n = len(arr)
    # Build a max heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i, h)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        comp += 1
        arr[i], arr[0] = arr[0], arr[i]  # swap
        swap += 1
        heapify(arr, i, 0, h)
    return arr, comp, swap


while True:
    a = input('Как заполняем массив?\n'
              '<1 - Ввести значения>\n'
              '<2 - Сгенерировать псевдослучайный массив>\n'
              '>>> ')
    arr = np.zeros(1000, dtype=int)
    if a == '1':
        try:
            arr = np.array(input('Введите массив для сортировки: ').split(','), dtype=int)
        except IndexError:
            print('Введите элементы массива через запятую!')
            continue
    elif a == '2':
        arr = np.array(rnd.sample(range(10000), 10000), dtype=int)
    else:
        print('Нет, выберите что-то из предложенного!')
        continue
    print('Какую сортировку будем тестировать ?(Введите номер)')
    print('=' * 33)
    choice = input('||<1 - bubble_sort>            ||\n'
                   '||<2 - selection_sort>         ||\n'
                   '||<3 - insertion_sort>         ||\n'
                   '||<4 - cocktail_sort>          ||\n'
                   '||<5 - shell_sort>             ||\n'
                   '||<6 - heap_sort>              ||\n'
                   '||<7 - Проверить все алгоритмы>||\n'
                   '=================================\n'
                   '>>> ')
    how = int(input('В каком порядке сортировать ?\n'
                    '<1 - По возрастанию>\n'
                    '<2 - По убыванию>\n'
                    '>>> '))
    if choice == '1':
        print('=' * 100)
        t = clock()
        r = bubble_sort(arr, how)
        print('Отсортированный:{}. Время сортировки: {}'.format(arr, str(clock() - t)))
        print('Данный алгоритм совершил: {} сравнений | {} перестановок.'.format(r[1], r[2]))
        print('=' * 100)
    elif choice == '2':
        print('=' * 100)
        t = clock()
        selection_sort(arr, how)
        r = selection_sort(arr, how)
        print('Отсортированный:{}. Время сортировки: {}'.format(arr, str(clock() - t)))
        print('Данный алгоритм совершил: {} сравнений | {} перестановок.'.format(r[1], r[2]))
        print('=' * 100)
    elif choice == '3':
        print('=' * 100)
        t = clock()
        insertion_sort(arr, how)
        r = insertion_sort(arr, how)
        print('Отсортированный:{}. Время сортировки: {}'.format(arr, str(clock() - t)))
        print('Данный алгоритм совершил: {} сравнений | {} перестановок.'.format(r[1], r[2]))
        print('=' * 100)
    elif choice == '4':
        print('=' * 100)
        t = clock()
        cocktail_sort(arr, how)
        r = cocktail_sort(arr, how)
        print('Отсортированный:{}. Время сортировки: {}'.format(arr, str(clock() - t)))
        print('Данный алгоритм совершил: {} сравнений | {} перестановок.'.format(r[1], r[2]))
        print('=' * 100)
    elif choice == '5':
        print('=' * 100)
        t = clock()
        shell_sort(arr, how)
        r = shell_sort(arr, how)
        print('Отсортированный:{}. Время сортировки: {}'.format(arr, str(clock() - t)))
        print('Данный алгоритм совершил: {} сравнений | {} перестановок.'.format(r[1], r[2]))
        print('=' * 100)
    elif choice == '6':
        print('=' * 100)
        t = clock()
        heap_sort(arr, how)
        r = heap_sort(arr, how)
        print('Отсортированный:{}. Время сортировки: {}'.format(arr, str(clock() - t)))
        print('Данный алгоритм совершил: {} сравнений | {} перестановок.'.format(r[1], r[2]))
        print('=' * 100)
    elif choice == '7':
        print('Таблица эффективности'.rjust(63))
        print('Название алгоритма  ||' + '  Количество сравнений || ' +
              '  Количество перестановок || ' + '    Время выполнения(c)      || ')
        print('=' * 107)
        t = clock()
        r = bubble_sort(arr, how)
        print('Bubble sort         ||', r[1],
              ' ' * 18, ' || ', r[2], ' ' * 21
              , ' || ', str(clock() - t))
        t = clock()
        r = selection_sort(arr, how)
        print('Selection sort      ||', r[1],
              ' ' * 18, ' || ', r[2],
              ' ' * 21, ' || ', str(clock() - t))
        t = clock()
        r = insertion_sort(arr, how)
        print('Insertion sort      ||', r[1],
              ' ' * 18, ' || ', r[2], ' ' * 21,
              ' || ', str(clock() - t))
        t = clock()
        r = ''
        r = cocktail_sort(arr, how)
        print('Cocktail shaker sort||', r[1],
              ' ' * 18, ' || ', r[2], ' ' * 21,
              ' || ', str(clock() - t))
        t = clock()
        r = ''
        r = shell_sort(arr, how)
        print('Shell sort          ||', r[1],
              ' ' * 18, ' || ', r[2], ' ' * 21,
              ' || ', str(clock() - t))
        t = clock()
        r = heap_sort(arr, how)
        print('Heap sort           ||', r[1],
              ' ' * 18, ' || ', r[2], ' ' * 21,
              ' || ', str(clock() - t))
        print('=' * 107)
    else:
        print('Такого пункта нету! Сделайте свой выбор.')
        continue
    if input('Press Enter to continue...') != '':
        break
