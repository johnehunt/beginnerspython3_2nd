temperatures = [12.4, 18.2, 15.4, 17.8, 13.1, 19.0, 12.3]
print(f'temperatures: {temperatures}')

# Sort function
# Sort into ascending order
print(f'sorted temperatures: {sorted(temperatures)}')

# Print out the result of sorting the temperatures into descending order (without modifying the original list).
print(f'sorted temperatures descending order: {sorted(temperatures, reverse=True)}')

# Print out the result of sorting the original list into ascending order.
temperatures.sort()
print(f'sorted temperatures: {temperatures}')

# Print out the result of sorting the original list into descending order.
temperatures.sort(reverse=True)
print(f'sorted temperatures descending order: {temperatures}')

print('+' * 25)

records = [('Monday', '12:00', 12.4),
           ('Tuesday', '12:00', 18.2),
           ('Wednesday', '13:00', 15.4),
           ('Thursday', '11:45', 17.8),
           ('Friday', '12:15', 13.1)]
print(f'records: {records}')

# Sort into ascending order
print(f'sorted records: {sorted(records, key=lambda temp: temp[2])}')

# Print out the result of sorting the temperatures into descending order (without modifying the original list).
print(f'sorted records descending order: {sorted(records, key=lambda temp: temp[2], reverse=True)}')

# Print out the result of sorting the original list into ascending order.
records.sort(key=lambda temp: temp[2])
print(f'sorted temperatures: {records}')

# Print out the result of sorting the original list into descending order.
records.sort(key=lambda temp: temp[2], reverse=True)
print(f'sorted temperatures descending order: {records}')
