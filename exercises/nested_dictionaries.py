people = {
    'jb24': {
     'first_name': 'james',
     'last_name': 'buchanan',
     'age': 24
    },
    'mb22': {'first_name': 'mhairi',
     'last_name': 'brudenell',
     'age': 22
    },
    'ab21': {'first_name': 'angus',
     'last_name': 'buchanan',
     'age': 21
    },
    'br25': {'first_name': 'brice',
     'last_name': 'riddell',
     'age': 25
    },
}

for username, details in people.items():
    print(f'Username: {username}')
    print(f'\tFirst name: {details["first_name"].title()}')
    print(f'\tLast name: {details["last_name"].title()}')