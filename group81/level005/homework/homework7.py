password = 1234
guess = int(input('enter your password:'))

while password != guess:
    print('password is inccorect')
    guess = int(input('enter your password:'))
else:
    print('access granted!')

