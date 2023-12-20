def build_profile(first, last, **user_info):
    '''
    Build a dictionary containing everythin we know about a user.
    '''

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('james', 'buchanan', job = 'data analyst', favourite_food = 'pizza')
print(user_profile)