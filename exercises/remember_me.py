from pathlib import Path
import json

def get_stored_username(path):
    '''Retrives stored username if present.'''
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else: 
        return None
            
def get_new_username(path):
    username = input('Please enter a username: ')
    contents = json.dumps(username)
    path.write_text(contents)
    return username
        
def greet_user():
    '''Greet user by username.'''
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f'Welcome back {username}')
    else:
        get_new_username(path)
        print(f"We'll remember you for next time {username}!")
        
greet_user()