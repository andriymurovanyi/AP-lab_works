from enum import Enum as e
import sys


class color(e):
    Green = 1
    Red = 2
    Yellow = 3
    White = 4
    Black = 5


class animal(e):
    Rat = 1
    Cow = 2
    Tiger = 3
    Rabbit = 4
    Dragon = 5
    Snake = 6
    Horse = 7
    Sheep = 8
    Monkey = 9
    Chicken = 10
    Dog = 11
    Pig = 12
flag = True
while flag:
    year = input('Введите год: ')
    if year.isdigit():
        year = int(year)
        first = -56
        c = True
        if year < 0:
            print('Введите год нашей эры')
            continue
        else:
            while c:
                for i in color:
                    for j in animal:
                        if year == first:
                            print('По старояпонскому: ', color(i).name, animal(j).name)
                            c = False
                            break
                        first += 1
                    break
    else:
        try:
            year = float(year)
            print('Год должен быть целым числом!')
            continue
        except ValueError:
            print('Год должен быть числом!')
            continue
    while True:
        x = input('Try again? [y/n]').lower()
        if x == 'y':
            break
        elif x == 'n':
            sys.exit()
