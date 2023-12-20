def car_info(manufacturer, model_name, **car_information):
    car_information['manufacturer'] = manufacturer
    car_information['model'] = model_name
    return car_information

jeep_info = car_info(
    manufacturer = 'jeep', 
    model_name = 'wrangler', 
    colour = 'red',
    doors = 2
)

{print(f'{key.title()}: {value}') for key, value in jeep_info.items()}