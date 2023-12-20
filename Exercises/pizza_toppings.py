def pizza_maker(requested_toppings):
    '''
    prints toppings that are put on pizza
    '''

    availible_toppings = ['pepper', 'onion', 'sweetcorn', 'tomato', 'olive']
    counter = 1

    for topping in requested_toppings:
        if topping in availible_toppings:
            if counter < 5:
                counter += 1
                print(f'Adding {topping} to your pizza!')
            else:
                print(f'You have reached the topping limit!')
                break
        else:
            print('Sorry, that topping is unavailable!')

pizza_maker(['sweetcorn', 'pepper', 'olive', 'peperoni', 'tomato', 'olive', 'olive'])