password = input('Enter password to check stength: ')

if len(password) < 7:
    print('Weak Password.')

elif len(password) > 7:
    if any(char in '!@&_' for char in password):
        print('Strong Password.')

    else:
        print('Medium Password.')