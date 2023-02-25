"""Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you'll add that topping to their pizza."""

prompt = "\nPlease enter the name of your pizza toppings:"
prompt += "\n(Enter 'quit' when yor are finished.) "

while True:
    message = input(prompt)

    if message == "quit":
        break
    else:
        print(f"\nI'll add the {message} topping to your pizza.")