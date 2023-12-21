from car_info_function import car_info

jeep = car_info('jeep', 'wrangler', colour = 'red')

{print(f'{key.title()}: {value}') for key, value in jeep.items()}

