from pathlib import Path

def word_counter(filenames: list, word: str):
    print(f'Count of string "{word}":')
    for file in filenames:
        contents = Path(file).read_text()
        print(f'- "{file}": {contents.count(word)}')
        
        
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']
word_counter(filenames, 'the ')