def build_person(first_name, last_name, age = None, job = None):
    '''
    Returns a dictionary of information about a person.
    '''
    person = {'first': first_name.title(),
              'last': last_name.title(),
              'age': age}
    if job:
        person['job'] = job

    return person

print(build_person('james', 'buchanan', 24))