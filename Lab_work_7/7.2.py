# Murovany Andriy. KNIT16-A.
# Дан текст из строчных русских букв. Между соседними словами - запятая, 
# за последним словом - точка. Вывести на экран все глухие согласные буквы, 
# которые не входят хотя бы в одно слово.
from re import search
letters = {'к', 'п', 'т', 'с', 'ф', 'х', 'ц', 'ч', 'ш'}

while True:
    sent = input('Введите предложение (через запятую)'
                 'и поставьте в конце точку: ').lower()
    if ',' not in sent:
        print('Слова должны быть через запятую!')
        continue
    else:
        if not sent.endswith('.'):
            print('Поставьте в конце точку!')
            continue
        else:
            if not search('[А-Яа-я]', sent):
                print('Должны быть русскоязычные слова!')
            else:
                sent.replace('.', '')
                a = set(sent)
                print(set(sorted(letters - a)))
    if input('Tap Enter key to continue...') != '':
        break
