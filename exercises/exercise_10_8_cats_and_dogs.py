from pathlib import Path

filenames = ['cats.txt', 'dogs.txt', 'birds.txt']

# [print(f'- "{Path(file)}"') for file in filenames]

try:
    for file in filenames:
        print(f'\nFile: "{file}"')
        contents = Path(file).read_text()
        contents = contents.splitlines()
        [print(f'- "{line}"') for line in contents]
except FileNotFoundError:
    print(f'- "{file}" does not exist.')