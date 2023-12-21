age_prompt = 'Please enter your age: '
user_age = input(age_prompt)

if int(user_age) >= 18:
    name_prompt = 'If you share your name, we can personalise the messages you see.'
    name_prompt += '\nWhat is your name?: '
    name = input(name_prompt)
    print(f'Hello {name}!')
else:
    print('Sorry, you must be 18 or over to play.')