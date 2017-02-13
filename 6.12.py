from enum import Enum as e


class measure(e):
    decimetre = 1
    kilometre = 2
    metre = 3
    milimetre = 4
    centimetre = 5


class converter(e):  # Избавляемся от непосредственных переменных.
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
        if p == measure.kilometre:
            x *= converter.kilometre.value
        elif p == measure.decimetre:
            x /= converter.decimetre.value
        elif p == measure.milimetre:
            x /= converter.milimetre.value
        elif p == measure.centimetre:
            x /= converter.centimetre.value
        elif p == measure.metre:
            x = x
        print('Metre lenght: {}'.format(x))
    while True:
        x = input('Try again? [y/n]').lower()
        if x == 'y':
            break
        elif x == 'n':
            flag = False
            break
