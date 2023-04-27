# set up some containers for use with Frozensets
tuple1 = (1, 2, 3, 4, 3, 2)
list1 = ['A', 'B', 'C', 'B', 'A']
dict1 = {'Wales': 'Cardiff',
         'England': 'London',
         'Scotland': 'Edinburgh'}
set1 = {'apple', 'orange', 'banana'}

fs1 = frozenset(tuple1)
print(f'tuple1: {tuple1}')
print(f'fs1: {fs1}')

print('-' * 10)

fs2 = frozenset(list1)
print(f'list1: {list1}')
print(f'fs2: {fs2}')

print('-' * 10)

fs3 = frozenset(dict1)
print(f'dict1: {dict1}')
print(f'fs3: {fs3}')

print('-' * 10)

fs4 = frozenset(set1)
print(f'set1: {set1}')
print(f'fs4: {fs4}')

print('-' * 10)

# Frozenset operations
brands = frozenset(['ford', 'jaguar', 'bmw'])
manufacturers = brands.copy()
print(f'brands: {brands}')
print(f'manufacturers: {manufacturers}')

# Equality
print(f'brands == manufacturers: {brands == manufacturers}')
print(f'brands == fs3: {brands == fs3}')
print('-' * 10)

fruit = frozenset(['apple', 'pear', 'banana'])
veg = frozenset(['carrot', 'cabbage', 'peas'])
print(f'fruit.union(veg): {fruit.union(veg)}')

breakfast = frozenset(['apple', 'strawberry', 'banana'])
print(f'fruit.intersection(breakfast): {fruit.intersection(breakfast)}')

print(f'fruit.difference(breakfast): {fruit.difference(breakfast)}')

owner = frozenset(['jaguar', 'bmw'])
print(f'breakfast.issubset(fruit): {owner.issubset(brands)}')


