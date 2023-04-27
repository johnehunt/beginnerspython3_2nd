name = 'John'
data = [1, 2, 3, 4]
info = ('a', 'b', 'c')
cities = cities = {'Wales': 'Cardiff',
                   'England': 'London'}

print(f'len(name): {len(name)}')
print(f'len(data): {len(data)}')
print(f'len(info): {len(info)}')
print(f'len(cities): {len(cities)}')


class Bag:
    def __init__(self, owner, items):
        self.owner = owner
        self.items = items

    def __len__(self):
        return len(self.items)


bag1 = Bag('John', [])
print(f'len(bag1): {len(bag1)}')
