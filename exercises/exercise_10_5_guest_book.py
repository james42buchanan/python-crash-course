from pathlib import Path

print('Please enter names to the list of guests.')
print('Enter "finished" to exit.\n')
    
names = ''
while True:
    name = input('Please enter your name: ')
    if name.lower() == 'finished':
        break
    else:
        names += name + ','
names = names.rstrip(',')

path = Path('name.txt')
path.write_text(names)