letters = {'к', 'п', 'т', 'с', 'ф', 'х', 'ц', 'ч', 'ш'}
import re

while True:
    sent = input('Введите предложение (через запятую) и поставьте в конце точку: ')
    a = set()
    if not re.search('[А-Яа-я]', sent):
        print('Должны быть русскоязычные слова!')
    else:
        wrd = sent.split(',')
        for i in letters:
            for j in wrd:
                if i not in j:
                    a.add(i)
        print(sorted(a))
