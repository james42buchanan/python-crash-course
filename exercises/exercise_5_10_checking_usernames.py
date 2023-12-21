current_users = ['S11JB3', 's12lg3', 's10lm5', 's11cs0', 's12fd3', 's10qw4']
new_users = ['s13ab2', 's10qw4', 's14kk9', 's11jb3']

def make_lowercase(list):
    new_list = []
    for item in list:
        new_list.append(item.lower())
    return new_list

def is_availible(usernames):
    make_lowercase(usernames)
    for name in new_users:
        if name.lower() in current_users:
            print(f'Username "{name}" already exists, please enter something else')
        else:
            print(f'Username {name} is availible, welcome!')

is_availible(new_users)