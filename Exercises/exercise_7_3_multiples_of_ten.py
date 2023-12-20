number = int(input("Tell me a number and I'll tell you if it's divisible by ten: "))

if number % 10 == 0:
    print(f'{number} is divisible by 10')
else:
    print(f'{number} is not divisible by ten')