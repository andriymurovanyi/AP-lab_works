import sys
days = range(1, 32)
mounths = range(1, 13)
years = range(1901, 2016)
flag = True
while flag:
    try:
        d, m, y = int(input('Day: ')), int(input('Mounth: ')), int(input('Year: '))
    except ValueError:
        print('Day must be integer number')
        continue
    if d in days and m in mounths and y in years:
        if d + 1 not in days:
            d = 1
            if m + 1 not in mounths:
                m = 1
                y += 1
            else:
                m += 1
        print('Date of the next day: {}.{}.{}'.format(d, m, y))

    else:
        print('Data out of range!')

    while True:
        x = input('Try again? [y/n]').lower()
        if x == 'y':
            break
        elif x == 'n':
            sys.exit()