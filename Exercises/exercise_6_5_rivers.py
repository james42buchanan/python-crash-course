rivers = {
    'seine': 'france',
    'rhine': 'germany',
    'thames': 'england'
}

for river, country in rivers.items():
    print(f'The river {river.title()} flows in {country.title()}')

print('\n')
for river in rivers:
    print(river.title())

print('\n')
for country in rivers.values():
    print(country.title())