from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
lines = contents.splitlines()

# line_counter = 0
# for line in lines:
#     print(f'{line_counter}: {line}')
#     line_counter += 1
        
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(f'Length: {len(pi_string)}')
