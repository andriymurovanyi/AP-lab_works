import re
letters = {'к', 'п', 'т', 'с', 'ф', 'х', 'ц', 'ч', 'ш'}
while True:
    sent = input('Введите предложение (через запятую) и поставьте в конце точку: ')
    if ',' not in sent:
        print('Слова должны быть через запятую!')
        continue
    else:
        if not sent.endswith('.'):
            print('Поставьте в конце точку!')
            continue
        else:
            if not re.search('[А-Яа-я]', sent):
                print('Должны быть русскоязычные слова!')
            else:
                sent.replace('.', '')
                a = set(sent)
                print(set(sorted(letters - a)))
    if input('Tap Enter key to continue...') != '':
        print()
        break
