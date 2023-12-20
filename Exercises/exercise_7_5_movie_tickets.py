print('Welcome to the movies!\nEnter "quit" to exit the program.\n')

age = int(input('Please enter your age: '))
if age == 'quit':
    active = False
elif age < 3:
    print('You may enter for free')
    active = False
elif age < 12:
    print('Your ticket is £10')
elif age > 12:
        print('Your ticket is £15')