
class Item:
    def __init__(self, name, country, count):
        self.name = name
        self.country = country
        self.count = count


class Items:
    def __init__(self):
        self.items = []
    
    def addItem(self, item):
        self.items.append(item)
        
    def getContries(self, item_name):
        summa = 0
        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                a = self.items[i].country
                summa += self.items[i].count
        if summa == 0:
                print('Товар не экспортировался или его нету в базе!')
        else:
            print('Товар экспортировался в {} в кол-ве {} штук'.format(a, summa))

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

while True:
    ans = input('<1 - Посмотреть каталог товаров>\n'
                '<2 - Смотреть информацию об эскпорте>\n'
                '<3 - Добавить свой товар>\n')
    if ans == '1':
        pass
    elif ans == '2':
        try:
            items.getContries(input('Введите название товара: '))
        except ValueError:
            print('Нужно ввести название товара!')
    elif ans == '3':
        i_new = Item(input('Введите название товара: '),
                     input('Введите страну: '),
                     int(input('Введите количество: ')))
        items.addItem(i_new)
        continue
    if input('Press Enter to continue...') != '':
        break

