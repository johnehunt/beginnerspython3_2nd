# Uses of structural matching in python

# Simple matcher style
def greeter(language):
    if language == 'English':
        print('Hello')
    elif language == 'Spanish':
        print('Hola')
    elif language == 'French':
        print('Bonjour')
    elif language == 'German':
        print('Hallo')


greeter('Spanish')


def greeter2(language):
    match language:
        case 'English':
            print('Hello')
        case 'Spanish':
            print('Hola')
        case 'French':
            print('Bonjour')
        case 'German':
            print('Hallo')


greeter2('Spanish')


def greeter2a(language):
    match language:
        case 'English':
            print('Hello')
        case 'Spanish':
            print('Hola')
            print('Buenas')
        case 'French':
            print('Bonjour')
        case 'German':
            print('Hallo')


greeter2a('Spanish')


def get_status_message(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 418:
            return "I'm a teapot"
        case _:
            return 'Something is wrong'


print(get_status_message(404))
print(get_status_message(401))


# handle unknown values
def greeter3(language):
    match language:
        case 'English':
            print('Hello')
        case 'Spanish':
            print('Hola')
        case 'French':
            print('Bonjour')
        case 'German':
            print('Hallo')
        case _:
            print('Unknown language')


greeter3('Welsh')


# Pick up an unknown value
def greeter4(language):
    match language:
        case 'English':
            print('Hello')
        case 'Spanish':
            print('Hola')
        case 'French':
            print('Bonjour')
        case 'German':
            print('Hallo')
        case unknown:
            print(f'Language {unknown} is not yet known to us')


greeter4('Welsh')


# Or patterns

def greeter5(language):
    match language:
        case 'English' | 'American':
            print('Hello')
        case 'Spanish':
            print('Hola')
        case 'French':
            print('Bonjour')
        case 'German':
            print('Hallo')
        case unknown:
            print(f'Language {unknown} is not yet known to us')


greeter5('English')
greeter5('American')


# matching sequences such as a list or tuple
# Tuples - can match on tuple values


def locator(point):
    match point:
        case (0, 0):
            print('Corner')
        case (0, y):
            print(f'Left edge at x=0, y={y}')
        case (x, 0):
            print(f'Top edge at x={x}, y=0')
        case (x, y):
            print(f'Point in grid at x={x}, y={y}')
        case _:
            raise ValueError('Not a point tuple')


cursor = (0, 0)
locator(cursor)
cursor = (0, 10)
locator(cursor)
cursor = (10, 0)
locator(cursor)
cursor = (10, 5)
locator(cursor)


def banking_operation1(action):
    match action:
        case ['balance']:
            print('Getting the balance')
        case ['deposit', amount]:
            print(f'Depositing {amount}')
        case ['withdraw', amount]:
            print(f'Withdrawing {amount}')


banking_operation1(['balance'])
banking_operation1(['deposit', 12.55])
banking_operation1(['withdraw', 9.99])


def banking_operation2(action):
    match action:
        case ['balance']:
            print('Getting the balance')
        case ['deposit', amount]:
            print(f'Depositing {amount}')
        case ['withdraw', amount]:
            print(f'Withdrawing {amount}')
        case ['deposit', *amounts]:
            print(f'Depositing multiple amounts - {amounts}')


banking_operation2(['deposit', 2.51, 9.44])
banking_operation2(['deposit', 2.51, 9.44, 3.21, 5.76])
banking_operation2(['deposit'])


def banking_operation3(action):
    match action:
        case ['help'] | ['info']:
            print('Help information')
        case ['balance']:
            print('Getting the balance')
        case ['deposit', amount]:
            print(f'Depositing {amount}')
        case ['withdraw', amount]:
            print(f'Withdrawing {amount}')
        case ['deposit', *amounts]:
            print(f'Depositing multiple amounts - {amounts}')


banking_operation3(['help'])
banking_operation3(['info'])


def direction(actions):
    match actions:
        case ['go', ("north" | "south" | "east" | "west")]:
            print('Going north or south or east or west')


direction(['go', 'north'])


def direction2(actions):
    match actions:
        case ['go', ("north" | "south" | "east" | "west") as towards]:
            print(f'Going {towards}')


direction2(['go', 'north'])

# Adding conditionals to patterns
VALID_DIRECTIONS = ["north", "south", "east", "west"]


def handle_command(command):
    match command:
        case ['go', direction] if direction in VALID_DIRECTIONS:
            print(f'Going {direction}')
        case _:
            print('Wrong direction')


handle_command(['go', 'east'])
handle_command(['go', 'north-east'])
