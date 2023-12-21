# This program will check if people are tall enough to go on a rollercoaster ride

heights_meters = {'James': 1.71, 'Mhairi': 1.68, 'Angus': 1.7, 'Bobby': 1.77, 'Brice': 1.75, 'Jay': 1.74, 'Chavdar': 1.8}

def rollercoaster_height(heights, limit):
    tall_enough = dict()
    not_tall_enough = dict()


    for customer, value in heights.items():
        if len(tall_enough) < 5:
            if value < limit:
                not_tall_enough.setdefault(customer, value)
            else:
                tall_enough.setdefault(customer, value)
        else:
            print('Ride full!')
            
    return print(f'''
    Customers: {sorted(heights_meters.items())}
    Total customers {len(heights_meters)}
    Tall enough and on ride: ({len(tall_enough)}) people: {tall_enough}
    Too short: ({len(not_tall_enough)}) people: {not_tall_enough}
    ''')

rollercoaster_height(heights_meters, 1.7)