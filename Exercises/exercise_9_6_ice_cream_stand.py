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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name):
        super().__init__(restaurant_name)
        self.flavours = ['vanilla', 'mint', 'chocolate', 'peanut']

    def show_flavours(self):
        print('Availible flavours:')
        [print(f'- {flavour.title()}') for flavour in self.flavours]

james_cream = IceCreamStand("james' cream")

james_cream.show_flavours()