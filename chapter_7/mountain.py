# filling a dictionary with User Input

# Create a empty dictionary
responses = {}

# set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # prompt for the person's name and response
    name = input("\nWhat's your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # store the response in a dictionary
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no): ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
