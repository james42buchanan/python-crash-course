from pathlib import Path

contents = input('Please enter your name: ')

path = Path('name.txt')
path.write_text(contents)