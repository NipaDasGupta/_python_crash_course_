'''Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.'''

sandwich_orders = ['tuna sandwich', 'pastrami sandwich', 'chicken sandwich',
                'pastrami sandwich', 'egg sandwich', 'pastrami sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I will make your {current_order}.")
    finished_sandwiches.append(current_order)

"""No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches."""

print(f"\nThe deli has run out of pastrami.")
while 'pastrami sandwich' in finished_sandwiches:
    finished_sandwiches.remove('pastrami sandwich')

print(f"\nThe following sandwiches ordered have been made:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)