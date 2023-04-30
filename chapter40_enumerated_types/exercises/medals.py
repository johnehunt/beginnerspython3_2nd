from enum import Enum


class Medals(Enum):
    GOLD = 1
    SILVER = 2
    BRONZE = 3


print('Starting')
position = 1
while True:
    athlete_name = input('Please enter the athletes name: ')
    if athlete_name == '':
        break
    athlete_medal = 'no medal'
    if position == 1:
        athlete_medal = Medals.GOLD
    elif position == 2:
        athlete_medal = Medals.SILVER
    elif position == 3:
        athlete_medal = Medals.BRONZE
    print(f'{athlete_name} obtained {athlete_medal}')
    position = position + 1

print('Done')
