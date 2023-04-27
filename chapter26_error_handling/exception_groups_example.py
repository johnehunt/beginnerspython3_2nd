def do_something():
    eg = ExceptionGroup("multiple exceptions occurred",
                       (ValueError("incorrect value"),
                        ValueError("not a positive value"),
                        FileNotFoundError("Unknown file data.txt"),
                        AttributeError("date")))
    raise eg


try:
    do_something()
except* ValueError as exp_group:
    print('ValueErrors:')
    print(exp_group.exceptions)
except* FileNotFoundError as exp_group:
    print('FileNotFoundErrors:')
    for e in exp_group.exceptions:
        print(e)
# except* AttributeError as exp_group:
#     print('AttributeError')
#     print(exp_group.exceptions)
