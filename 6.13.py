import sys
from enum import Enum as e


class Country(e):
    Germany = 1
    Cuba = 2
    Laos = 3
    Monaco = 4
    Banglades = 5
    Ukraine = 6


class Continent(e):
    Asia = 1
    America = 2
    Europe = 3


count_cont = {  # Соответствие страны определенному континенту.(Country - Continent)
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
}
flag = True
while flag:
    try:
        s = Continent(count_cont[Country[input('country: ')].value]).name
    except KeyError:
        print('Country not found!')
        continue
    else:
        print('Continent: {}'.format(s))
    while True:
        x = input('Try again? [y/n]').lower()
        if x == 'y':
            break
        elif x == 'n':
            sys.exit()


