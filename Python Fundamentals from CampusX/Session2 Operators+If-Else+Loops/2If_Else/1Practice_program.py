#Log in program and identation
#email -> fahadsorkar@gmail.com
#pass -> K@nek1k3n#

email = input('Enter email: ')
password = input('Enter password: ')

if email=='fahadsorkar23@gmail.com' and password == 'K@nek1k3n#':
    print('Welcome')
elif email == 'fahadsorkar23@gmail.com' and password != 'K@nek1k3n#':
    print('Correct email but incorrect password')
    password = input('Enter password again: ')
    if password == 'K@nek1k3n#':
        print('Welcome')
    else:
        print('You can\'t do this, go fuck yourself')
else:
    print('Not correct, Try again')
