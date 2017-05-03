def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


a = int(input('a = '))
b = int(input('b = '))
print('НОД =', nod(a, b))
