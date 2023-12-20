cities = {
    'aberdeen': {
        'country': 'scotland',
        'poulation': 198_590,
        'fact': 'also known as the "granite city"'
        },
    'edinburgh': {
        'country': 'scotland',
        'population': 506_520,
        'fact': "capital city of scotland"
        },
    'glasgow': {
        'country': 'scotland',
        'population': 635_130,
        'fact': 'most populous city in scotland'
        }
}

for city, information in cities.items():
    print(f'{city.title()}')
    for metric, info in information.items():
            print(f'\t{metric.title()}:\t{info}')