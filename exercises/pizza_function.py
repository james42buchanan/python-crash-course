def make_pizza(size, *toppings):
    '''
    Summarise the pizza we are about to make.
    '''

    print(f'Making a {size} pizza with the following toppings:')
    [print(f'- {topping.title()}') for topping in toppings]