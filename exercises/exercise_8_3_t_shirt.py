def make_shirt(size = 'large', message = 'I love Python'):
    print(f'Making a {size} t-shirt.')
    if message:
        print(f'Printing "{message}" on t-shirt.')

make_shirt(size = 'small')
