print('Give me two numbers and i will divide them.')
print('Enter "q" to quit.')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Error: You cannot divide by zero!')
    except ValueError:
        print('Input must be an intiger!')
    else:
        print(answer)