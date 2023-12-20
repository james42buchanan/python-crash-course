class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f'User first name: {self.first_name}, last name: {self.last_name}')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!\n')
    
s11jb3 = User('james', 'buchanan')
s11jb3.describe_user()
s11jb3.greet_user()

s11mb2 = User('mhairi', 'brudenell')
s11mb2.describe_user()
s11mb2.greet_user()

s11jd1 = User('joseph', 'demathias')
s11jd1.describe_user()
s11jd1.greet_user()