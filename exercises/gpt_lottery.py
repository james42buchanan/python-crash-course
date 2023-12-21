import random
import string

def generate_lottery_ticket():
    # Generate a pseudo-random lottery ticket with alphanumeric characters
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def check_lottery_tickets(ticket1, ticket2):
    # Check if the two lottery tickets match
    return ticket1 == ticket2

def main():
    player_ticket = generate_lottery_ticket()
    winning_ticket = generate_lottery_ticket()

    attempts = 0

    while not check_lottery_tickets(player_ticket, winning_ticket):
        # Generate a new lottery ticket for the player
        player_ticket = generate_lottery_ticket()

        attempts += 1

        print(f"Attempt {attempts}: Player's Ticket: {player_ticket}")

    print(f"Congratulations! You won in {attempts} attempts.")
    print(f"Winning Ticket: {winning_ticket}")

if __name__ == "__main__":
    main()