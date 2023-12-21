import random

        
def play_lottery():
    '''
    Play a game of the lottery with one ticket.
    '''
    
    possible_letters = ['a', 'b', 'c', 'd']
    possible_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    winning_ticket = list()
    while len(winning_ticket) < 6:
        winning_ticket.append(random.choice(possible_numbers))
        winning_ticket.append(random.choice(possible_letters))
    
    your_ticket = list()
    while len(your_ticket) < 6:
        your_ticket.append(random.choice(possible_numbers))
        your_ticket.append(random.choice(possible_letters))
    
    if your_ticket == winning_ticket:
        return True
    else:
        return False


# playing the lottery until I win
lottery_counter = 0
while play_lottery() is False:
    lottery_counter += 1
    print(f'Count of non-winning tickets: {lottery_counter}')
print(f'You won the lottey after {lottery_counter} attempts!')