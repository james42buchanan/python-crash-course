def addition():
 

    while True:
        print("Enter two numbers and I'll print the answer.")
        print("Enter 'q' to exit.")

        first_number = input('Please enter your first number: ')
        if first_number == 'q':
            break
        second_number = input('Please enter your second number: ')
        if second_number == 'q':
            break
        try:
            result = float(first_number) + float(second_number)
        except ValueError:
            print('You must enter two numbers!')
        else:
            print(f'The answer is {result}.\n')

addition()