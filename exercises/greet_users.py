def greet_users(names):
    '''
    Prints a greeting message to every member of a list.
    '''

    [print(f'Hello {name.title()}!') for name in names]


friends = ['james', 'michael', 'brenda', 'dave']
greet_users(friends)