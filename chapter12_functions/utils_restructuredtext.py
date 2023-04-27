def get_integer_input(message):
    """
     This function will display the message to the user
      and request that they input an integer.

    :param message: The message to print
    :returns: the integer entered by the user

    """
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)

    return int(value_as_string)


response = get_integer_input("Please input total: ")
print(f'The response is {response}')
