'''
This module contains the User, Admin, and Privileges classes.
There model a network admin, users, and their associated privileges.
'''

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f'User first name: {self.first_name}, last name: {self.last_name}')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!\n')


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges = [
            "Delete comments.",
            "Ban users.",
            "Promote users.",
            "Delete group.",
            "Promote other users."
            ]):
        self.privileges = privileges

    def show_privileges(self):
        print('Admin privileges:')
        [print(f'- {privilege.title()}') for privilege in self.privileges]