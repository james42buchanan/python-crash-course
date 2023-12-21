prompt = '\nEnter "quit" to exit the program.'
prompt += '\nEnter a city you have visited: '

cities = []
while True:
    city = input(prompt)
    if city == "quit" or len(cities) == 3:
        print('\nNo more cities!')
        break
    else:
        cities.append(city)
        [print(f'I like {city.title()}') for city in cities]
