#  Murovanyi Andriy. KNIT16-A
#  Вывести кол-во чисел, которые входят в последовательность один раз.
flag = True
while flag:
    try:
        posl = sorted(input('Введите числа через пробел: ').split())
    except ValueError:
        print('Введите числа через пробел!')
        continue
    else:
        for i in posl:
            if not str(i).isdigit():
                print('Вы должны ввести числа!')
                break
        else:
            a = set()
            for i in posl:
                if posl.count(i) == 1:
                    a.add(i)
            print('Уникальных элементов: {}'.format(len(a)))
    while True:
        x = input('Try again ? [y/n]').lower()
        if x == 'y':
            break
        elif x == 'n':
            flag = False
            break




















