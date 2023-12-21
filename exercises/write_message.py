from pathlib import Path

contents = 'i love programming.\n'
contents += 'i also love creating new games.\n'
contents += 'i also love working with data.\n'

path = Path('programming.txt')
path.write_text(contents)