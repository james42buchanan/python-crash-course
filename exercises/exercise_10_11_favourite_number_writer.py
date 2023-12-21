from pathlib import Path
import json

path = Path('favourite_number.json')
favourite_number = input('Please enter your favourite number: ')
contents = json.dumps(int(favourite_number))
path.write_text(contents)