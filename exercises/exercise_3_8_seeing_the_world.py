places = ['ullapool', 'cambridge', 'germany', 'new zealand', 'transylvania']

print(f'''
Original: {places}
Sorted: {sorted(places)}
Reverse sorted: {sorted(places, reverse = True)}
''')

places.reverse()
print(f'Reversed original: {places}')

places.reverse()
print(f'Reversed twice: {places}')

places.sort()
print(f'.sort(): {places}')

places.sort(reverse = True)
print(f'.sort(reverse = True): {places}')