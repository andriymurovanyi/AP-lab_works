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
        V = 0
        x = []

        for i in range(len(self.items)):
            if self.items[i].name == item_name:
                x.append(self.items[i].country)
                V += self.items[i].count
        if V == 0:
            print('Product wasn\'t exported or it is absented in Database!')
        else:
            print('This product was exported in {}.Overall volume: {}'.format(x, V))
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
print('Welcome to app of our export company!\n')
print('Countries, which worked with us: ')
for i in Countries.__members__:
    print(i)
print()
while True:
    print('Choose, what you want to do:\n'
          '<1 - See product catalog>\n'
          '<2 - See information about export>\n'
          '<3 - Add new products>')
    ans = input('Your selection is...: ')
    if ans == '1':
        print('Our products: ')
        for i in sorted(app):
            print(i)
    elif ans == '2':
        try:

            items.GetCountries(input('Input a name of product: '))
        except ValueError:
            print('You must input a name of product!')
            continue
    elif ans == '3':
        a = input('Input a name of product: ')
        b = input('Input country: ')
        c = int(input('Input a quantity: '))
        if a.isalpha() and b.isalpha() and b in Countries.__members__:
                i_new = Item(a, b, c)
                items.addItem(i_new)
        else:
            print('Maybe you\'re input is incorrect? Check it!')
            continue
    inp = input('Press Enter to continue or smth to leave the program...')
    if inp != '':
        break
    else:
        continue
