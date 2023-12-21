def is_even(number):
    if number % 2 == 0:
        return f'{number} is even'
    else:
        return f'{number} is odd'

number = int(input('Please input a number: '))
print(is_even(number))