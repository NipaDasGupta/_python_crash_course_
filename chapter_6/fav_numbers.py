favorite_numbers = {
    'nipa' : 7,
    'john' : 1,
    'peter' : 2,
    'isabel' : 4,
}

number = favorite_numbers.get('nick', "Username is unavailable.")
print(number)

'''Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Then print each person's
name along with their favorite numbers.'''

favorite_numbers = {
    'nipa' : [7, 0, 1],
    'john' : [1, 0],
    'peter' : [2],
    'isabel' : [4, 3, 0],
}

for person, favorite_numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")
    for favorite_number in favorite_numbers:
        print(f"{favorite_number}")