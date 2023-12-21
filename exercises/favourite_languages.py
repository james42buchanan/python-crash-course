favourite_languages = {
    'jen': ['python', 'java', 'swift'],
    'sarah': ['c', 'c++'],
    'edward': ['rust', 'go'],
    'phil': ['r'],
}

# friends = ['jen', 'edward', 'phil', 'sarah', 'jennifer']
# take_poll = []
# for friend in sorted(friends):
#     if friend in favourite_languages:
#         language = favourite_languages[friend]
#         print(f'Hello {friend.title()}! I see you code in {language.title()}')
#     else:
#         print(f'Hello {friend.title()}! Please take our programming language poll!')
#         take_poll.append(friend)

# for person in take_poll:
#     print(f'\nStill to take poll: {person.title()}')

# print('\n')
# for friend in friends:
#     if friend not in take_poll:
#         print(f'Thank you {friend.title()} for taking the programming language poll!')

# for friend, language in favourite_languages.items():
#     print(f"{friend.title()}'s favourite programming language(s): {language}")

for friends, languages in favourite_languages.items():
    if len(languages) > 1:
        print(f"{friends.title()}'s favourite programming languages are:")
        for language in languages:
            print(f'\t{language.title()}')
    else:
        print(f"{friends.title()}'s favourite programming languages is:")
        for language in languages:
            print(f'\t{language.title()}')