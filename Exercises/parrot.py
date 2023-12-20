prompt = "Enter 'quit' to exit the program."
prompt += "\nType something and I'll repeat it: "

active = True
message = ''

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f'{message}\n')