pizzas = ['pepperoni', 'jalapeno', 'olive']
friend_pizzas = pizzas[:]

pizzas.append('pepper')
friend_pizzas.append('pineapple')

for pizza in pizzas:
    print(f'I like {pizza.title()} pizza')

[print(f'My friend likes {pizza.title()} pizza') for pizza in friend_pizzas]