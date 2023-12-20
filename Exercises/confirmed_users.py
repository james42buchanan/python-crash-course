unconfirmed_users = ['james', 'mhairi', 'angus', 'bobby']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print(f'Verifying {current_user.title()}...')

print('\nVerified users:')
[print(f'\t{user.title()}') for user in confirmed_users]