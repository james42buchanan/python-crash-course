class Restaurant:
    '''
    A model of a restaurant.
    '''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'This restaurant is called {self.restaurant_name}, it serves {self.cuisine_type.title()} food!')
    
    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open!')

    def number_of_customers(self):
        print(f'Number of people served: {self.number_served}')
    
    def set_number_served(self, number):
        self.number_served = number
        print(f'{number} people have been served.')

    def increment_number_served(self, number):
        self.number_served += number
        print(f'{number} additional people have been served.')


itsu = Restaurant('itsu', 'japanese')
itsu.number_of_customers()
itsu.set_number_served(14)
itsu.increment_number_served(14)
itsu.number_of_customers()
