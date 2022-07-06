for attempts_left in range(3, 0, -1):
    password = input('Enter your password: ')
    if password == '98eaxc':
        print('Access granted')
        break
else:
    print('Access denied')
    
