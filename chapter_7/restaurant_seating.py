"""Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message
saying they'll have to wait for a table. Otherwise, report that their table is
ready."""

restaurant_seating = input("How many people are in your dinner group? ")
restaurant_seating = int(restaurant_seating)

if restaurant_seating >= 8:
    print(f"\nYou'll have to wait for a table to be ready.")
else:
    print(f"\nThe table is ready.")
