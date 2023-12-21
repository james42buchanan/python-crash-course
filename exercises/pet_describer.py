def describe_pet(pet_name, animal_species = 'dog'):
    '''
    Prints species and name of pet
    '''

    print(f'I have a pet {animal_species}.')
    print(f"It's name is {pet_name.title()}!")


describe_pet(pet_name = 'tom', animal_species = 'bat')