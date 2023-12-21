def get_formatted_name(first_name, last_name):
    '''
    Return a full formatted name.
    '''

    full_name = f'{first_name} {last_name}'
    return full_name.title()


while True:
    print('\nEnter "quit" at any time to exit')
    print('Please enter your name: ')

    first_name = input('First name: ')
    if first_name.lower() == 'quit':
        break

    last_name = input('Last name: ')
    if last_name.lower() == 'quit':
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print(f'Hello {formatted_name}!')