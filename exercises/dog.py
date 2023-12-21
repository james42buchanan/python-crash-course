class Dog:
    '''
    A simple attempt to model a dog.
    '''

    def __init__(self, name, age):
        '''
        Initialise name and age attributes.
        '''
        self.name = name
        self.age = age
    
    def sit(self):
        '''
        Simulate a dog sitting in response to a command.
        '''
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        '''
        Simulate a dog rolling over in response to a command.
        '''
        print(f'{self.name} is rolling over!')

my_dog = Dog('Wilbur', 12)
print(f'My dog is called {my_dog.name}.')
print(f'My dog is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Ziggy', 14)
print(f'\nYour dog is called {your_dog.name}.')
print(f'Your dog is {your_dog.age} years old.')
your_dog.sit()
your_dog.roll_over()