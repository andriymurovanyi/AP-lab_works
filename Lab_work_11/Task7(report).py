# Мурованый Андрей.КНИТ16-А
# Условие: Вывести в файл свою анкету.
import os
flag = True
while flag:
    os.chdir('D:/NewFold/')
    os.chdir('D:/NewFold/MyFold')
    print('Мы находимся в следующуей директории:', os.getcwd())
    print('Ну что, начнем анкетирование? :)')
    while True:
        name = input('Как Вас зовут ?\n'
                     '>>>')
        if not (name.isalpha() and name.istitle()):
            print('Нет, введите имя')
            flag = False
        else:
            year = input('Сколько Вам лет?\n'
                         '>>>')
            if int(year) not in range(10, 101):
                print('Вы допустили ошибку!')
                flag = False
            else:
                phone = input('Ваш номер телефона?\n'
                              '>>>')
                if phone[0:4] != '+380':
                    print('Ошибка ввода номера!')
                    flag = False
                else:
                    email = input('Ваш электронный адрес?\n'
                                  '>>>')
                    if not ('@' and '.') in email:
                        print('Вы допустили ошибку!')
                        flag = False
                    else:
                        with open('MyAnket.txt', 'w') as g:
                            g.write('Имя: ' + name + '\n')
                            g.write('Возраст: ' + year + '\n')
                            g.write('Моб. номер: ' + phone + '\n')
                            g.write('Электроннный адрес: ' + email + '\n')
                        with open('MyAnket.txt', 'r') as f:
                            line = f.readlines()
                        for i in line:
                            print(i, sep='')
        if input('Press Enter to continue...') != '':
            flag = False
            break
