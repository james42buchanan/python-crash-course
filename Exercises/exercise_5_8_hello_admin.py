# usernames = ['admin', 's11jb3', 's12lg3', 's10lm5', 's11cs0', 's12fd3']
usernames = []

if usernames:
    for name in usernames:
        if name != 'admin':
            print(f'Hello {name}!')
        else:
            print(f'Greetings admin')
else:
    print('No usernames to display')