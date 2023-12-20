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


class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_fuel_tank(self, fuel_volume):
        print('Electric cars do not have fuel tanks.')
    
    def check_fuel_volume(self):
        print('Electric cars do not have fuel tanks.')


class Battery:

    def __init__(self, battery_size = 40, miles_per_kwh = 4):
        self.battery_size = battery_size
        self.miles_per_kwh = miles_per_kwh

    def describe_battery(self):
        print(f'This car has a battery capacity of {self.battery_size} kwh.')

    def get_range(self):
        if self.battery_size > 0:
            range = self.battery_size * self.miles_per_kwh
            print(f'This car can travel for approximately {range} miles on a full charge.')
        else:
            print('No or incorrect battery installed.')

    def set_miles_per_kwh(self, distance_per_kwh_charge):
        self.miles_per_kwh = distance_per_kwh_charge

    def set_battery_size(self, set_size):
        self.battery_size = set_size
        print(f'Battery size set to {set_size} kwh.')

    def upgrade_battery(self, upgrade_size = 25):
        self.battery_size += upgrade_size


my_electric_car = ElectricCar('nissan', 'leaf', 2022)
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()

my_electric_car.battery.set_miles_per_kwh(2)
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()