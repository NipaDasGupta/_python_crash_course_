"""A class that can be used to represent a lottery game."""
from random import choice

# Initializes a lottery's attributes."""
lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']


def pull_in(generate_ticket):
    """Pull the numbers or letters for the wining lottery ticket number."""
    wining_ticket = []
    for _ in range(4):
        pulled_in = str(choice(lottery))
        # don't add repatative numbers or letters
        if pulled_in not in wining_ticket:
            wining_ticket.append(pulled_in)
    return wining_ticket


def read_ticket(wining_ticket):
    """Prints a statement showing the wining lottery ticket number."""
    print(
        f"Any ticket matching these combination of {''.join(wining_ticket)} wins a prize!")


def check_ticket(generated_ticket, wining_ticket):
    """Match between the generated random ticket and your ticket."""
    for _ in generated_ticket:
        if _ not in wining_ticket:
            return False
    return True


def win_lottery():
    """Print a statement showing how many times it runs to match with your wining ticket."""
    my_ticket = ['a', 1, 'd', 2]
    runs = 0
    won = False
    MAX_TRIES = 100_000

    while not won:
        new_ticket = pull_in(lottery)
        won = check_ticket(new_ticket, my_ticket)
        runs += 1
        if runs >= MAX_TRIES:
            break

    if won:
        print("\nCongrats!")
        print(f"Your ticket number {my_ticket} is {won}-ly matched.")
        print(f"It runs {runs} times to win the lottery.")
    else:
        print("Please, try again!")
