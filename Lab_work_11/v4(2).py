# Мурованый Андрей.КНИТ16-А
# Записать в файл q копию файла f
from os import mkdir, getcwd, chdir
chdir('D:/NewFold/MyFold')
print('Мы находимся в следующуей директории:', getcwd())
while True:
    with open('f.txt', 'r') as f:
        line_f = f.read()
    print('Вот, что было в файле f: \n', line_f)
    with open('g.txt', 'w') as g:
        g.write(line_f[::-1])
    with open('g.txt', 'r') as op:
        line_g = op.readlines()
    print('Вот, что запишем в файл g:')
    for i in line_g:
        print(i, sep='')
    if input('Press Enter to continue...') != '':
        break




