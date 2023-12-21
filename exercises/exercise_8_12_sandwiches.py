def sandwich_fillings(*fillings):
    [print(f'{filling.title()}') for filling in fillings]

sandwich_fillings('hummus', 'tomato', 'black pepper')