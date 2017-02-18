from enum import Enum as e


class measure(e):  # Избавляемся от непосредственных переменных.
    decimetre = 0.1
    kilometre = 1000
    metre = 1
    milimetre = 0.001
    centimetre = 0.01


flag = True
while flag:
    try:
        x = float(input('lenght: '))
        p = measure[input('measure: ')]
    except (KeyError, ValueError):
        print('Key or Value error!')
        continue
    else:
        print('Metre lenght: {}'.format(x * p.value))
    while True:
        x = input('Try again? [y/n]').lower()
        if x == 'y':
            break
        elif x == 'n':
            flag = False
            break