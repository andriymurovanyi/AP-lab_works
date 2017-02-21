import re
letters = {'к', 'п', 'т', 'с', 'ф', 'х', 'ц', 'ч', 'ш'}

flag = True
while flag:
    c = 0
    sent = input('Введите предложение (через запятую) и поставьте в конце точку: ')
    a = set(sent)
    if ',' not in sent or not sent.endswith('.'):
        print('Проверьте знаки препинания!')
    else:
        if not re.search('[А-Яа-я]', sent):
            print('Должны быть русскоязычные слова!')
        else:
            wrd = sent.split(',')
            print(sorted(letters - a))
    if input('Tap Enter key to continue...') != '':
        break
