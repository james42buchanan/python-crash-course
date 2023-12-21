'''
This module represents a lottery.
'''

import random
import string

class Lottery():
    '''
    Represents a lottery game that generates pseudo-random lottery tickets.
    '''
    
    def __init__(self):
        pass
    
    @staticmethod
    def random_ticket():
        '''
        Creates a pseudo-random alphanumeric ticket.
        '''
                
        random_alphanumeric = [random.randrange(0, 9),
                               random.choice(string.ascii_lowercase)]

        ticket = list()
        while len(ticket) < 6:
            ticket.append(random.choice(random_alphanumeric))
        return ticket
    
    @staticmethod
    def play_lottery():
        '''
        Play a game of the lottery with one ticket.
        '''

        if __class__.random_ticket() == __class__.random_ticket():
            return True
        else:
            return False
    
    @staticmethod
    def play_until_win():
        '''
        Plays lottery until a winning ticket is generated.
        '''
        
        lottery_counter = 0
        while __class__.play_lottery() is False:
            lottery_counter += 1
            print(f'Loses: {lottery_counter}')
        print(f'You won the lottey after {lottery_counter} tickets!\n')