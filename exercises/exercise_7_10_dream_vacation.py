responses = dict()

polling_active = True
while polling_active:
    print('If you could go on holiday anywhere in the world, where would you go?')
    name = input('\tPlease enter your name: ')
    destination = input('\tPlease enter your destination: ')
    responses[name] = destination

    repeat = input('New poll? (enter yes or no): ')
    if repeat == 'no':
        polling_active = False

print('\nPolling results')
{print(f'{name.title()} would go to {destination.title()}!') for name, destination in responses.items()}