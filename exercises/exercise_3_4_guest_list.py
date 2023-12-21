# setting which guests can or cannot attend
guest_list = ['charles darwin', 'limmy', 'epictetus']
replacement_guest = 'richard dawkins'
cannot_attend = 'charles darwin'


# printing guests who can attend
for guest in guest_list:
    print(f'Dear {guest.title()}, you are invited to my dinner party!\n')
    if guest == cannot_attend:
        guest_list.remove(cannot_attend)
        print(f'\t{cannot_attend.title()} unfortunately cannot attend, he is dead.\n\n\t{replacement_guest.title()} will attend instead!\n')

# checks whether bigger table can be found
bigger_table = True
new_guests = ['marcus aurelius', 'noam chomsky', 'earth worm jim']

if bigger_table == True:
    print('\tA bigger table has been found!\n')
    # guest_list.insert(0, new_guests[0])
    # guest_list.insert(2, new_guests[1])
    # guest_list.append(new_guests[2])
    print(f'{new_guests[0].title()}, {new_guests[1].title()}, and {new_guests[2].title()} have been invited to the party!\n')

for guest in new_guests:
    print(f'Dear {guest.title()}, you are invited to my dinner party!\n')

print('Oh no!, the resturaut will only allow me to invite two guests!\n')

[guest_list.append(guest) for guest in new_guests]

print(f'''Number of invited guests: {len(guest_list)}\n''')

while len(guest_list) != 2:
    guest_list.pop()

[print(f'\tDear {guest}, you are still invited to my party!\n') for guest in guest_list]

del guest_list[0:]

print(f'Remaining guests: {guest_list}')