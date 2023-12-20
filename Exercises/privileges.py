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