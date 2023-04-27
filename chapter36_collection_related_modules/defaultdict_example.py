from collections import defaultdict

# Basic functionality of Defaultdict

days = defaultdict(lambda: -1)
days['Monday'] = 1
days['Tuesday'] = 2

print(days['Monday'])
print(days['Tuesday'])
print(days['Wednesday'])


def default_value():
    return 'Not Known'

# Defining the dict
cities = defaultdict(default_value)
cities['England'] = 'London'
cities['Wales'] = 'Cardiff'

print(cities['England'])
print(cities['Wales'])
print(cities['Ireland'])
