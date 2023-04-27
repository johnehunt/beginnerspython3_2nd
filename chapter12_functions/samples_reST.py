
def get_input(prompt):
    """This function is primarily used to illustrate reST, for example:
    This is used for *emphasis* while this is used for **bold**. Finally
    this is used for a literal ``result``.
    """
    result = input(prompt)
    return result


print(get_input("please enter a value: "))


def get_more_input(prompt):
    """This function is used to illustrate lists, for example:

    * This is a bulleted list.
    * It has two items, the second item uses two lines.

    1. This is a numbered list.
    2. It has two items too.

    #. This is a numbered list.
    #. It has two items too.

    """
    result = input(prompt)
    return result


print(get_more_input("name: "))


def get_something(prompt):
    """
    We can use lists:

    * this is
    * a list

        * with a nested list
        * and some subitems

    * and here the parent list continues

    :param prompt: the input prompt
    :return: the value entered by the user
    """
    result = input(prompt)
    return result


def get_another_thing(prompt):
    """
    To use this function see the code block::

        result = get_another_thing("please input data: ")
        print(result)

    This is back to normal text
    """
    result = input(prompt)
    return result

