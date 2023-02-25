"""Dream Vacation: Write a program that polls users about their dream vacation.
Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll."""
responses = {}

polling_active = True
while polling_active:
    users = input(f"\nWhat's your name? ")
    response = input(
        f"\nIf you could visit one place in the world, where would you go? ")

    responses[users] = response

    # find out if anyone else is going to take the poll
    repeat = input(
        f"\nWould you like to let another person respond? (yes/no): ")
    if repeat == 'no':
        polling_active = False

print(f"--- Poll Results ---")
for user, response in responses.items():
    print(f"{user.title()} would like to climb {response.title()}.")
