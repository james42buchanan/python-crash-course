from random import randint

class Die:
    '''
    Represents a die of a specified number of sides.
    '''
    
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self, roll_number):
        '''
        Represents the random roll of a die with a specified number of sides.
        '''
        
        number_list = list()
        die_counter = 0
        while die_counter < roll_number:
            die_counter += 1
            number_list.append(randint(1, self.sides))
        return number_list
    

die1 = Die(4)
print(f'My random numbers: {die1.roll_die(10)}')