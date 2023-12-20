from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding = 'utf-8')
except FileExistsError:
    print(f'Sorry the file {path} does not exist.')
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file "{path}" has approximately {num_words} words.')