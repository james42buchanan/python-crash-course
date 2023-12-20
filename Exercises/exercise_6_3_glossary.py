glossary = {
    'int': 'Refers to an intiger value, otherwise known as a "whole" number.',
    'str': 'Refers to the "string" data type. Usually contains word-values, but may contain any characters.',
    'for_loop': 'Refers to a programming procedure that performs an iterated operation of every item of a list.',
    'if_statement': 'Refers to a programming procedure where single or multiple conditions must be satisfied for evaluation to equal True. True conditions must be met for code to continue.',
    'list': 'Also known as an "array", a list contains a set of non-unique values in an indexed order.',
    'set': 'Refers to a mutable data structure of unique, non-ordered values.',
    'dictionary': 'Also known as a hash map/table, a dictionary stores key-value pairs, allowing lookups.',
    'f-string': r'Refers to "format strings" where an "f/F" is placed in front of a string, allowing python code to be evaluated within {}.',
    'r-string': 'Refers to "string literal" where an "r/R" is placed in front of string to escape all characters and evaluate string exactly.',
    'dynamic_typing': 'Refers to how data types are assigned in programming languages, e.g. Python: data types are not explicityly typed, but approximated at run-time',
}

for term, definition in glossary.items():
    print(f'{term}: "{definition}"\n')