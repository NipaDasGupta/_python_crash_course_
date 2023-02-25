person_0 = {
    'first_name': 'john',
    'last_name': 'smith',
    'age': 18,
    'city': 'san Francisco',
}

# print(person_0)

'''People: Start with the program you wrote for Exercise 6-1 (page 99).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.'''

person_1 = {
    'first_name': 'nipa',
    'last_name': 'das gupta',
    'age': 24,
    'city': 'chittagong',
}

person_2 = {
    'first_name': 'ada',
    'last_name': 'lovelace',
    'age': 25,
    'city': 'london',
}

people = [person_0, person_1, person_2]

for person in people:
    print(person)