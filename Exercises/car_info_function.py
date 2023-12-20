def car_info(manufacturer, model_name, **car_information):
    car_information['manufacturer'] = manufacturer
    car_information['model'] = model_name
    return car_information