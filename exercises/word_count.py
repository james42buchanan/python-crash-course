from pathlib import Path

def count_words(path):
    '''
    Count the approximate number of words in a file.
    '''
    missing_fies = list()

    try:
        contents = path.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        missing_fies.append(path)
        # pass
        # print(f'File "{path}" does not exist.')
    else:
        # Count the approximate number of words in each file.
        words = contents.split()
        num_words = len(words)
        print(f'File "{path}" has approximately {num_words} words.')

    # print('\nThe following files could not be read:')
    # [print(f'- {file}') for file in missing_fies]


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'catcher_in_the_rye.txt']
[count_words(Path(file)) for file in filenames]