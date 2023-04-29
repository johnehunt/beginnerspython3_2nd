
def do_something():
    try:
        # code raising a ValueError
        raise ValueError('Value Incorrect')
    except ValueError as err:
        err.add_note('Invalid age')
        raise err


# do_something()

try:
    do_something()
except ValueError as err:
    print(err)
    print(err.__notes__)