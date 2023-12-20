responses = dict()

polling_active = True
while polling_active:
    name = input('\nPlease enter your name: ')
    response = input("Please enter the mountain you'd like to climb: ")
    responses[name] = response
    repeat = input('Poll again? (yes/no): ')
    if repeat == 'no':
        polling_active = False

print('\n--- Poll Results ---')
{print(f'{name.title()} would like to climb {response.title()}') for name, response in responses.items()}