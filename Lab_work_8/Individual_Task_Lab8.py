import random as rnd
from enum import Enum
import numpy as np


class DataBaseTovar(Enum):
    computers = {
        'Ukraine': 2,
        'Russia': 3,
        'England': 4
    }
    medicine = {
        'China': 5,
        'USA': 6,
        'Portugal': 8
    }
    clothing = {
        'Italy': 9,
        'France': 10,
        'Germany': 11
    }
    toys = {
        'Germany': 17,
        'USA': 18,
        'Turkey': 20
    }
    software = {
        'USA': 18,
        'China': 10,
        'Germany': 11
    }
    meal = {
        'Ukraine': 56,
        'Slovakia': 57,
        'Portugal': 43
    }
    furniture = {
        'China': 32,
        'Moldova': 48,
        'USA': 49
    }
    books = {
        'Ukraine': 100,
        'USA': 130,
        'Slovakia': 135
    }
    smartphones = {
        'Germany': 55,
        'China': 30,
        'England': 26
    }

c = True
while c:
    ans = input('<1 - Посмотреть каталог товаров>\n'
                '<2 - Смотреть информацию об эскпорте>\n')
    if ans == '1':
        for catalog in DataBaseTovar.__members__:
            print(catalog)
    elif ans == '2':
        goods = input('Выберите товар: ')
        if goods.isdigit():
            print('Введите название товара!')
            continue
        else:
            if DataBaseTovar.__members__.__contains__(goods):
                for i in DataBaseTovar:
                    if str(goods) in str(i):
                        b = list(i.value.keys())  # Страны.
                        c = list(i.value.values())  # Кол-во товара.
                        V = 0
                        for j in c:  # Общий обьем экспорта.
                            j = int(j)
                            V += j
                        print('Товар \'{}\' экспортировался в {}. '
                              'Общий обьем: {} '.format(goods, b, V))
            else:
                print('Данного товара нету в каталоге!')
    while True:
        restart = input('Выйти из программы?[y/n]').lower()
        if restart == 'y':
            c = False
            break
        elif restart == 'n':
            break
