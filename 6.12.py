from enum import Enum as e


class measure(e):
    decimetre = 1
    kilometre = 2
    metre = 3
    milimetre = 4
    centimetre = 5

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
            x *= 1000
        elif p == measure.decimetre:
            x /= 10
        elif p == measure.milimetre:
            x /= 1000
        elif p == measure.centimetre:
            x /= 100
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