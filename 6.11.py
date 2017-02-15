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
    else:
        if d not in days and m not in mounths and y not in years:
            print('Data out of range!')
        else:
            if d + 1 == 32:
                d = 1
                if m + 1 == 13:
                    m = 1
                    y += 1
                    print('Date of the next day: {}.{}.{}'.format(d, m, y))
                else:
                    m += 1
                    print('Date of the next day: {}.{}.{}'.format(d, m, y))
    while True:
        x = input('Try again? [y/n]').lower()
        if x == 'y':
            break
        elif x == 'n':
            sys.exit()