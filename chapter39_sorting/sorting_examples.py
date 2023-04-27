data = (5, 2, 8, 1, 9, 3)
print(data)

sorted_data = sorted(data)
print(sorted_data)

data_list = [7, 5, 9, 2, 1, 3]
print(data_list)

sorted_data_list = sorted(data_list)
print(sorted_data_list)

data_list_2 = [2.3, 5.6, 1.2, 1.1, 5.5]
print(data_list_2)
sorted_data_list_2 = sorted(data_list_2)
print(sorted_data_list_2)

string_list = ["John", "Denise", "Phoebe", "Adam"]
print(string_list)

sorted_string_list = sorted(string_list)
print(sorted_string_list)

mixed_list = [5, 1.2, 7.34, 4]
print(mixed_list)
sorted_mixed_list = sorted(mixed_list)
print(sorted_mixed_list)

mixed_list = [5, 1.2, 7.34, True, 4]
print(mixed_list)
sorted_mixed_list = sorted(mixed_list)
print(sorted_mixed_list)

print('=' * 25)
# Reverse sorting

data = (5, 2, 8, 1, 9, 3)
print(data)

sorted_data = sorted(data, reverse=True)
print(sorted_data)
print('-' * 25)

data_list = [7, 5, 9, 2, 1, 3]
print(data_list)

sorted_data_list = sorted(data_list, reverse=True)
print(sorted_data_list)
print('-' * 25)

data_list_2 = [2.3, 5.6, 1.2, 1.1, 5.5]
print(data_list_2)
sorted_data_list_2 = sorted(data_list_2, reverse=True)
print(sorted_data_list_2)
print('-' * 25)

string_list = ["John", "Denise", "Phoebe", "Adam"]
print(string_list)

sorted_string_list = sorted(string_list, reverse=True)
print(sorted_string_list)
print('-' * 25)

mixed_list = [5, 1.2, 7.34, True, 4]
print(mixed_list)
sorted_mixed_list = sorted(mixed_list, reverse=True)
print(sorted_mixed_list)

print('=' * 25)

# The sort method
data_list = [5, 2, 8, 1, 9, 3]
print(data_list)
data_list.sort()
print(data_list)

print('-' * 25)

data_list_2 = [2.3, 5.6, 1.2, 1.1, 5.5]
print(data_list_2)
data_list_2.sort()
print(data_list_2)
print('-' * 25)

string_list = ['John', 'Denise', 'Phoebe', 'Adam']
print(string_list)
string_list.sort()
print(string_list)
print('-' * 25)

mixed_list = [5, 1.2, 7.34, True, 4]
print(mixed_list)
mixed_list.sort()
print(mixed_list)

print('=' * 25)
# Reverse sort method

data_list = [5, 2, 8, 1, 9, 3]
print(data_list)
data_list.sort(reverse=True)
print(data_list)

print('-' * 25)

data_list_2 = [2.3, 5.6, 1.2, 1.1, 5.5]
print(data_list_2)
data_list_2.sort(reverse=True)
print(data_list_2)
print('-' * 25)

string_list = ['John', 'Denise', 'Phoebe', 'Adam']
print(string_list)
string_list.sort(reverse=True)
print(string_list)
print('-' * 25)

mixed_list = [5, 1.2, 7.34, True, 4]
print(mixed_list)
mixed_list.sort(reverse=True)
print(mixed_list)

print('=' * 25)
string_list = ['John', 'Denise', 'Phoebe', 'Adam']
print(f'string list: {string_list}')
sorted_string_list1 = sorted(string_list)
print(f'default ordering: {sorted_string_list1}')
sorted_string_list2 = sorted(string_list, key=lambda s: len(s))
print(f'sorting based on string length: {sorted_string_list2}')

print('-' * 25)
string_list = ['John', 'Denise', 'Phoebe', 'Adam']
print(f'string list: {string_list}')
string_list.sort(key=lambda s: len(s))
print(f'sorting based on string length: {string_list}')

print('-' * 25)
data = [('John', 55), ('Denise', 90), ('Phoebe', 76)]
print(data)
sorted_data = sorted(data)
print(sorted_data)
sorted_data2 = sorted(data, key=lambda i: i[1])
print(sorted_data2)
sorted_data3 = sorted(data, key=lambda i: i[1], reverse=True)
print(sorted_data3)

print('-' * 25)
data = [('John', 55), ('Denise', 90), ('Phoebe', 76)]
print(data)
data.sort(key=lambda i: i[1])
print(data)
data.sort(key=lambda i: i[1], reverse=True)
print(data)
