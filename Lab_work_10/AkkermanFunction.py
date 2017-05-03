def Akkerman(n, m):
    if n == 0:
        return m + 1
    elif n > 0 and m == 0:
        return Akkerman(n - 1, m)
    elif n > 0 and m > 0:
        return Akkerman(n - 1, Akkerman(n, m - 1))

while True:
    n = int(input('n = '))
    m = int(input('m = '))
    print('Значение функции: ', Akkerman(n, m))
    if input('Press Enter to continue...') != '':
        break

