'''Movie Tickets: A movie theater charges different ticket prices depending on
a person's age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.'''

prompt = input("Please enter your age: ")
prompt = int(prompt)

if prompt < 3:
    ticket = 'free'
elif 3 > prompt or prompt <= 12:
    ticket = '$10'
else:
    ticket = '$15'

print(f"The ticket is {ticket}.")