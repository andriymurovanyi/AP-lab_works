from enum import Enum

app = set()


class Countries(Enum):
    Poland = 1
    China = 2
    Germany = 3
    Ukraine = 4
    Russia = 5
    Italy = 6
    Slovakia = 7
    Portugal = 8
    Moldova = 9
    Turkey = 10


class Item:
    def __init__(self, name, country, count):
        self.name = name
        self.country = country
        self.count = count
        self.app = app.add(name)


class Items:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def GetCountries(self, item_name):
        summa = 0
        print('Страны, в которые экспортировался данный товар: ')
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                print(self.items[i].country)
                summa += self.items[i].count
        print('Общий обьем: ', summa)


items = Items()
i1 = Item('medicine', 'Poland', 10)
i2 = Item('computers', 'Ukraine', 20)
i3 = Item('furniture', 'China', 30)
i4 = Item('books', 'Italy', 15)
i5 = Item('smartphones', 'Germany', 15)
i6 = Item('toys', 'Ukraine', 15)
i7 = Item('books', 'Ukraine', 135)
i8 = Item('software', 'Poland', 15)
i9 = Item('toys', 'Germany', 15)
i10 = Item('furniture', 'Germany', 30)
items.addItem(i1)
items.addItem(i2)
items.addItem(i3)
items.addItem(i4)
items.addItem(i5)
items.addItem(i6)
items.addItem(i7)
items.addItem(i8)
items.addItem(i9)
items.addItem(i10)
print('Добро пожаловать в приложение нашей экспортной компании!\n')
while True:
    print('Выберите, что хотитите сделать:\n'
          '<1 - Посмотреть каталог товаров>\n'
          '<2 - Смотреть информацию об эскпорте>\n'
          '<3 - Добавить свой товар>')
    ans = input('Ваш ответ...: ')
    if ans == '1':
        print('Каталог наших товаров: ')
        for i in sorted(app):
            print(i)
    elif ans == '2':
        try:
            items.GetCountries(input('Введите название товара: '))
        except ValueError:
            print('Нужно ввести название товара!')
            continue
    elif ans == '3':
        a = input('Введите название товара: ')
        b = input('Введите страну: ')
        c = int(input('Введите колл-во: '))
        if a.isalpha() and b.isalpha() and b in Countries.__members__ :
                i_new = Item(a, b, c)
                items.addItem(i_new)
        else:
            print('Проверьте, возможно вы ввели что-то не так!')
            continue
    inp = input('Press Enter to continue or smth to leave the program...')
    if inp != '':
        break
    else:
        continue

