import numpy as np
import random as rnd
from timeit import timeit
import time


def effect(*args):
    setup = ''
    stmt = ''
    t = time.clock()
    return t - time.clock()


def bubble_sort(mass):
    """
    Bubble sort.

    Is a simple sorting algorithm that repeatedly steps through
    the list to be sorted, compares each pair of adjacent items
    and swaps them if they are in the wrong order.
    :param mass:
    :return:
    """
    n = 1
    while n < len(mass):
        for i in range(len(mass) - n):
            if mass[i] > mass[i + 1]:
                mass[i], mass[i + 1] = mass[i + 1], mass[i]
        n += 1
    return mass


def selection_sort(mass):
    """
    Selection sort.

     Selection sort is a sorting algorithm,
     specifically an in-place comparison sort.
    :param mass:
    :return:
    """
    for k in range(len(mass) - 1):
        m = k
        i = k + 1
        while i < len(mass):
            if mass[i] < mass[m]:
                m = i
            i += 1
        tmp = mass[k]
        mass[k] = mass[m]
        mass[m] = tmp
    return mass


def insertion_sort(mass):
    """
    Insertion sort.

     Insertion sort is a simple sorting algorithm that
     builds the final sorted array (or list) one item
     at a time.
    :param mass:
    :return:
    """
    for i in range(1, len(mass)):
        while i > 0 and mass[i] < mass[i - 1]:
            mass[i], mass[i - 1] = mass[i - 1], mass[i]
            i -= 1
    return mass


def cocktail_sort(mass):
    """
    Cocktail sort.

     Is a variation of bubble sort that is both a
     stable sorting algorithm and a comparison sort.
    :param mass:
    :return:
    """
    up = range(len(mass) - 1)
    while True:
        for i in (up, reversed(up)):
            c = False
            for j in i:
                if mass[j] > mass[j + 1]:
                    mass[j], mass[j + 1] = mass[j + 1], mass[j]
                    c = True
            if not c:
                return mass


def shell_sort(mass):
    """
    Shell sort.

     Is an in-place comparison sort
    :param mass:
    :return:
    """
    inc = len(mass) // 2
    while inc:
        for i, el in enumerate(mass):
            while i >= inc and mass[i - inc] > el:
                mass[i] = mass[i - inc]
                i -= inc
            mass[i] = el
        inc = 1 if inc == 2 else inc * 5 // 8
    return mass


def heap_sort(mass):
    """
    Heapsort.

    Heapsort can be thought of as an improved selection sort:
     like that algorithm, it divides its input into a sorted
     and an unsorted region, and it iteratively shrinks the
     unsorted region by extracting the largest element and
     moving that to the sorted region.
    :param mass:
    :return:
    """
    def heapify(mass):
        start = (len(mass) - 2) // 2
        while start >= 0:
            siftDown(mass, start, len(mass))
            start -= 1

    def siftDown(mass, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 < end and mass[child] < mass[child + 1]:
                child += 1
            if child <= end and mass[root] < mass[child]:
                mass[root], mass[child] = mass[child], mass[root]
                root = child
            else:
                return

    heapify(mass)
    end = len(mass) - 1
    while end > 0:
        mass[end], mass[0] = mass[0], mass[end]
        siftDown(mass, 0, end - 1)
        end -= 1
    return mass

while True:
    print('Выберите способ заполнения:\n'
          '<1 - Ввести значения самому>\n'
          '<2 - Сгенерировать псевдослучайную последовательность>\n')
    a = input()
    if a == '1':
        mass = np.array(input('Введите массив для сортировки: ').split(', '), dtype=int)
        print(heap_sort(mass))
    elif a == '2':
        mass = np.array(rnd.sample(range(1000), 100), dtype=int)
        print('Входной массив:\n{}\n'.format(mass),
              'Отсортированный:\n{}'.format(heap_sort(mass)))
    if input('Press Enter to continue...') != '':
        break