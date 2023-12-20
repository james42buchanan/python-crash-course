buffet_foods = ('apples', 'falafel', 'hummus', 'crisps', 'sandwiches')
buffet_foods = ('pears', 'falafel', 'hummus', 'crisps', 'sandwiches')

favourite_foods = ['falafel', 'pizza', 'hummus']

for food in buffet_foods:
    if food in favourite_foods:
        print(f"I'll have some {food} please!")
    else:
        print(f"There's {food} at the buffet")