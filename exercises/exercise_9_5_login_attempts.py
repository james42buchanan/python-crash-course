class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print(f'User first name: {self.first_name}, last name: {self.last_name}')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!\n')

    def increment_login_attempts(self, login_increment):
        self.login_attempts += login_increment

    def reset_login_attempts(self, set_number_of_logins):
        self.login_attempts = set_number_of_logins

    def show_login_attempts(self):
        print(f'Number of login attempts: {self.login_attempts}')

s11jb3 = User('james', 'buchanan')
s11jb3.increment_login_attempts(1)
s11jb3.show_login_attempts()
s11jb3.increment_login_attempts(1)
s11jb3.show_login_attempts()
s11jb3.increment_login_attempts(1)
s11jb3.show_login_attempts()
