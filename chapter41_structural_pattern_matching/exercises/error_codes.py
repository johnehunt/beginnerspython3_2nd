print('Starting')
while True:
    error_code = input('Please enter the error code: ')
    if error_code == '':
        break
    match error_code:
        case '400':
            print('Bad Request')
        case '401':
            print('Unauthorized')
        case '403':
            print('Forbidden')
        case '404':
            print('Not Found')
        case '418':
            print("I'm a teapot")
        case '429':
            print('Too Many Requests')
        case unknown:
            print(f'{unknown} - is an unknown error code')
print('Done')