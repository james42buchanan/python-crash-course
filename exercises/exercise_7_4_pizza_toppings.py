availible_toppings = ['pepper', 'onion', 'sweetcorn', 'tomato', 'olive']
chosen_toppings = []

print('Availible toppings:')
[print(f'\t{topping.title()}') for topping in availible_toppings]
print('\nEnter "done" when finished!\n')

active = True
while active == True:
    new_topping = (input('Enter a new topping: ')).lower()
    if new_topping == 'quit':
        break
    elif new_topping == 'done':
        print("\nHere's your pizza!:")
        [print(f'\t{topping.title()}') for topping in chosen_toppings]
        
        active = False
    else:
        if new_topping in availible_toppings:
            chosen_toppings.append(new_topping)
        else:
            print('Not availible!')
            continue
