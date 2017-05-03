import numpy as np
import random as rnd
import time

comp = 0
swap = 0

def bubble_sort(arr):
    global comp, swap
    """
    Bubble sort.

    Is a simple sorting algorithm that repeatedly steps through
    the list to be sorted, compares each pair of adjacent items
    and swaps them if they are in the wrong order.
    :param arr:
    :return:
    """
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            comp += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap += 1
        n += 1
    return arr


def selection_sort(arr):
    """
    Selection sort.

     Selection sort is a sorting algorithm,
     specifically an in-place comparison sort.
    :param arr:
    :return:
    """
    for k in range(len(arr) - 1):
        m = k
        i = k + 1
        while i < len(arr):
            if arr[i] < arr[m]:
                m = i
            i += 1
        tmp = arr[k]
        arr[k] = arr[m]
        arr[m] = tmp
    return arr


def insertion_sort(arr):
    """
    Insertion sort.

     Insertion sort is a simple sorting algorithm that
     builds the final sorted array (or list) one item
     at a time.
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


def cocktail_sort(arr):
    """
    Cocktail sort.

     Is a variation of bubble sort that is both a
     stable sorting algorithm and a comparison sort.
    :param arr:
    :return:
    """
    up = range(len(arr) - 1)
    while True:
        for i in (up, reversed(up)):
            c = False
            for j in i:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    c = True
            if not c:
                return arr


def shell_sort(arr):
    """
    Shell sort.

     Is an in-place comparison sort
    :param arr:
    :return:
    """
    inc = len(arr) // 2
    while inc:
        for i, el in enumerate(arr):
            while i >= inc and arr[i - inc] > el:
                arr[i] = arr[i - inc]
                i -= inc
            arr[i] = el
        inc = 1 if inc == 2 else inc * 5 // 8
    return arr


def heap_sort(arr):
    """
    Heapsort.

    Heapsort can be thought of as an improved selection sort:
     like that algorithm, it divides its input into a sorted
     and an unsorted region, and it iteratively shrinks the
     unsorted region by extracting the largest element and
     moving that to the sorted region.
    :param arr:
    :return:
    """
    def heapify(arr):
        start = (len(arr) - 2) // 2
        while start >= 0:
            siftDown(arr, start, len(arr))
            start -= 1

    def siftDown(arr, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 < end and arr[child] < arr[child + 1]:
                child += 1
            if child <= end and arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                return

    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        siftDown(arr, 0, end - 1)
        end -= 1
    return arr


while True:
    print('Выберите способ заполнения:\n'
          '<1 - Ввести значения самому>\n'
          '<2 - Сгенерировать псевдослучайную последовательность>\n')
    a = input()
    arr = np.zeros(1000, dtype=int)
    if a == '1':
        arr = np.array(input('Введите массив для сортировки: ').split(','), dtype=int)
    elif a == '2':
        arr = np.array(rnd.sample(range(10000), 10000), dtype=int)
    print('Какую сортировку будем тестировать ?(Введите номер)\n'
          '<1 - bubble_sort>\n'
          '<2 - selection_sort>\n'
          '<3 - insertion_sort>\n'
          '<4 - cocktail_sort>\n'
          '<5 - shell_sort>\n'
          '<6 - heap_sort>')
    ask = input()
    t = time.clock()
    if ask == '1':
        comp = 0
        swap = 0
        bubble_sort(arr)
    elif ask == '2':
        selection_sort(arr)
    elif ask == '3':
        insertion_sort(arr)
    elif ask == '4':
        cocktail_sort(arr)
    elif ask == '5':
        shell_sort(arr)
    elif ask == '6':
        heap_sort(arr)
    print('Отсортированный:{}. Время сортировки: {}'.format(arr, str(time.clock() - t)))
    print('Сравнений ', comp, 'Перестановок ', swap)
    if input('Press Enter to continue...') != '':
        break