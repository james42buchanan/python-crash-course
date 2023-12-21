'''
This module contains a class 'Car' used to represent combustion cars.
'''

class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel_tank_volume = 0
    
    def get_descriptive_name(self):
        '''
        Returns a descriptive formatted name.
        '''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        '''
        Print a statement about a car's mileage.
        '''
        print(f'This car has an odometer reading of {self.odometer_reading} miles.')

    def update_odometer(self, mileage):
        '''
        Set the odometer reading to a specific value.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer!")

    def increment_odometer(self, miles):
        '''
        Add the given amount to the odometer reading.
        '''
        if miles > 0:
            self.odometer_reading += miles
            print(f'Odometer updated by {miles} miles.')
        else:
            print("You cannot roll back an odometer!")

    def fill_fuel_tank(self, fuel_volume):
        self.fuel_tank_volume += fuel_volume
        print(f'{fuel_volume} litres of fuel added to tank.')
    
    def check_fuel_volume(self):
        print(f'Fuel in tank: {self.fuel_tank_volume} litres')