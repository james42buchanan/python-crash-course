def text_printer(unprinted_texts, printed_texts):
    import time
    while unprinted_texts:
        current_text = unprinted_texts.pop()
        printed_texts.append(current_text)
        print(current_text)
        time.sleep(1)
    print('\nAll messages printed!')
    

text_messages = [
    'Hello, how are you?',
    'When are you going to arrive?',
    'Thank you, goodbye!',
    'I will be there in 10 minutes.'
]

sent_messages = []

text_printer(text_messages[:], sent_messages)
print(text_messages)