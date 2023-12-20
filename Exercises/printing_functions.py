def printer(unprinted, printed):
    '''
    Prints the name of items and moves them to a new list with a 1 second delay
    '''

    import time
    while unprinted:
        current_design = unprinted.pop()
        printed.append(current_design)
        print(f'Printing {current_design.title()}...')
        time.sleep(1)
    print('\nAll items printed!:')
    

def show_printed(printed_designs):
    [print(f'\t - {design.title( )}') for design in printed_designs]