class Restaurant:
    '''
    A model of a restaurant.
    '''
    number_served = 0

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'This restaurant is called {self.restaurant_name}, it serves {self.cuisine_type.title()} food!')
    
    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open!')



itsu = Restaurant('itsu', 'japanese')
itsu.describe_restaurant()
itsu.open_restaurant()
