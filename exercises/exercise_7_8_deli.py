sandwich_orders = ['ham', 'cheese', 'pastrami', 'pastrami', 'butter', 'salad', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    new_order = sandwich_orders.pop()

    if new_order == 'pastrami':
        print('No more pastrami!')
    else:
        finished_sandwiches.append(new_order)
        print(f'Your {new_order.title()} sandwich is ready!')
