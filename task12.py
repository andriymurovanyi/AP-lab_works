"""Мурованый Андрей. КНИТ16-А
Индивидуальное задание №10 (б)
Условие: Программа. Дана последовательность, содержащая от 2 до 12 слов, в каждом из которых
от 2 до 8 букв; между соседними словами - проблел, за последним словом - точка.
Вывести все слова, которые отличны от последнего и удалить последнюю букву последовательности
из каждого слова этой последоватеьности."""
flag = True
while flag:
    text = input('Напишите предложение от 2 до 12 слов и поставьте точку: ')
    if text.endswith('.'):
        c = 1
        text = text.replace('.', '')
        words = text.split()
        if len(words) in range(2, 13):
            for k in words:
                if not 2 <= len(k) <= 8:
                    print('Должно быть от 2 до 8 букв!')
                    break
            else:
                while text.__getitem__(-c) == ' ':
                    c += 1
                else:
                    lw = text.__getitem__(-c)
                last = words.__getitem__(-1)
                for i in words:
                    if i != last:
                        print(i.replace(lw, ''), end=' ')
                else:
                    print(last.replace(lw, ''))
        else:
            print('Превышена длина!Должно быть от 2 до 12 слов! ')

    elif not text.endswith('.'):
        print('Должна быть точка!')
    while True:
        x = input('Try again? [y/n]').lower()
        if x == 'y':
            break
        elif x == 'n':
            flag = False
            break
