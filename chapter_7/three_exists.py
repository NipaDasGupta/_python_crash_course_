"""Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value.
"""

prompt = "\nPlease enter the name of your pizza toppings:"
prompt += "\n(Enter 'quit' when yor are finished.) "

active = True
while active:
    message = input(prompt)

    if message == "quit":
        break
    elif message == "french fries":
        print(f"\nSorry, we're out of {message}.")
        continue
    else:
        print(f"\nI'll add the {message} topping to your pizza.")