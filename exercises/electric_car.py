'''
This module contains a class 'Car' used to represent electric cars.
'''

from car import Car

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_fuel_tank(self, fuel_volume):
        print('Electric cars do not have fuel tanks.')
    
    def check_fuel_volume(self):
        print('Electric cars do not have fuel tanks.')


class Battery:

    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a battery capacity of {self.battery_size} kwh.')

    def get_range(self):
        
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 0
            print('Unknown range.')
        print(f'This car can travel for approximately {range} miles on a full charge.')

    def set_battery_size(self, set_size):
        self.battery_size = set_size
        print(f'Battery size set to {set_size} kwh.')