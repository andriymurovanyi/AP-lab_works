import pyparsing as pp
SIGN = '+-*'


def f(s, c=''):
    if len(s) != 0 and s[0].isdigit():
        return True
    elif (s[0] in SIGN) and (c in SIGN):
        return False
    else:
        return f(s[1:], s[0])

while True:
    try:

        s = input('Введите выражение, которое нужно проверить: ')
        if f(s):
            print('Данная запись является формулой!')
    except IndexError:
        print('Скорее всего, это не формула!')
    if input('Press Enter to continue...') != '':
        break

