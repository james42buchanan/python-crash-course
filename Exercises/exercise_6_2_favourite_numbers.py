favourite_numbers = {
    'james': [42, 19, 66],
    'mhairi': 22,
    'angus': [16, 17, 18],
    'bobby': [99, 96, 69],
    'poppy': 84
}

for person, numbers in favourite_numbers.items():
    if(isinstance(numbers, list)):
        print(f"{person.title()}'s favourite numbers:")
        for number in numbers:
            print(f'\t{number}')
    else:
        print(f"{person.title()}'s favourite number:")
        print(f'\t{numbers}')