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
    if d in days and y in years and m in mounths:
        if d in range(1, 31):
            print('Date of the next day: ', d + 1, m, y)
        elif d == 31:
            print('Date of the next day: ', 1, m + 1, y)
        elif m == 12:
            print('Date of the next day: ', 1, 1 , y + 1)

    else:
        print('Data out of range!')

    while True:
        x = input('Try again? [y/n]').lower()
        if x == 'y':
            break
        elif x == 'n':
            sys.exit()


