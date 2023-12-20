import car as cv
import electric_car as ev

my_new_car = cv.Car('landrover', 'defender', 1980)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(400)
my_new_car.read_odometer()

my_electric_car = ev.ElectricCar('nissan', 'leaf', 2023)
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()