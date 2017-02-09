from enum import Enum as e
import sys


class color(e):
    Green = 0
    Red = 1
    Yellow = 2
    White = 3
    Black = 4


class animal(e):
    Rat = 0
    Cow = 1
    Tiger = 2
    Rabbit = 3
    Dragon = 4
    Snake = 5
    Horse = 6
    Sheep = 7
    Monkey = 8
    Chicken = 9
    Dog = 10
    Pig = 11
flag = True
while flag:
    year = input('Введите год: ')
    if year.isdigit():
        if int(year) > 0:
            year = int(year) % 60 - 4
            c = 0  # Номер нужного нам цвета.
            while year >= 12:
                year //= 12
                c += 1
            zh = year % 12  # zh - животное(Определяем его номер)
            print('По древнеяпонскому: ', color(c).name, animal(zh).name)
        else:
            print('Введите год нашей эры!')
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
