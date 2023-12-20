# alien_0 = {'colour': 'green',
#            'points': 5}
# alien_1 = {'colour': 'yellow',
#            'points': 10}
# alien_2 = {'colour': 'red',
#            'points': 15}

# aliens = [alien_0, alien_1, alien_2]

aliens = []
for alien_number in range(30):
    new_alien = {'colour': 'green',
                 'points': 5,
                 'speed': 'slow'}
    aliens.append(new_alien)

print(f'A total of {len(aliens)} aliens were created.')

for alien in aliens[0:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['points'] = 14
        alien['speed'] = 'fast'

for alien in aliens:
    print(alien)