# Мурованый Андрей. КНИТ16-А
# Условие: написать программу, определяющую, является ли текст
# правильной записью "формулы", которая записана в соответстивии
# с синтаксисом EBNF:
# Формула = цифра {Цифра} | (Формула Знак Формула).
# Знак = '+'|'-'|'*'
# Цифра = '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9'
import string
OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y)}


def parse(formula):
    """
    Проверка формулы.
    
    :param formula: Принимает формулу в виде строки
    :return: собирает число из строки и возвращает его.
    """
    number = ''
    for s in formula:
        if s in '1234567890.':  # если символ - цифра, то собираем число
            number += s
        elif number:  # если символ не цифра, то выдаём собранное число и начинаем собирать заново
            yield float(number)
            number = ''
        if s in OPERATORS or s in "()":  # если символ - оператор или скобка, то выдаём как есть
            yield s
    if number:  # если в конце строки есть число, выдаём его
        yield float(number)


def shunting_yard(formula):
    """
    Алгоритм "сортировочной станции."
    
    Перевод выражения из инфиксной нотации в обратную
    польскую нотацию, используя алгоритм "сортировочной 
    станции"
    :param formula: Принимает формулу в виде строки
    :return: элементы в обратной польской нотации.
    """
    stack = []  # Имитируем стек с помощью списка.
    for token in formula:
        # если элемент - оператор, то отправляем дальше все операторы из стека,
        # чей приоритет больше или равен пришедшему,
        # до открывающей скобки или опустошения стека.
        if token in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                yield stack.pop()
            stack.append(token)
        elif token == ")":
            # если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
            # а открывающую скобку выкидываем из стека.
            while stack:
                x = stack.pop()
                if x == "(":
                    break
                yield x
        elif token == "(":
            # если элемент - открывающая скобка, просто положим её в стек
            stack.append(token)
        else:
            # если элемент - число, отправим его сразу на выход
            yield token
    while stack:
        yield stack.pop()


def calc(polish):
    """
    
    :param polish: принимает формулу в обратной польской нотации
    :return: возвращает значение формулы.
    """
    stack = []
    for token in polish:
        if token in OPERATORS:  # если приходящий элемент - оператор,
            y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
            stack.append(OPERATORS[token][1](x, y))  # вычисляем оператор, возвращаем в стек
        else:
            stack.append(token)
    return stack[0]  # результат вычисления - единственный элемент в стеке

while True:
    try:
        formula = input('Введите выражение: ').replace('.', '')
    except (ValueError, IndexError):
        print('Проверте введенные данные!')
        continue
    if not("+" in formula or '*' in formula or '-' in formula):
        print('Проверьте, действительно ли введена формула...')
    else:
        for i in formula:
            if i in string.ascii_letters:
                print('В формуле не должно быть букв!')
                break
            else:
                print('Значие выражения: {}'.format(calc(shunting_yard(parse(formula)))))
                break
    if input('Press Enter to continue...') != '':
        break
