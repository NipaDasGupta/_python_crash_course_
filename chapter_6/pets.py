'''Pets: Make several dictionaries, where each dictionary represents a different
pet. In each dictionary, include the kind of animal and the owner's name. Store
these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.'''

pet_0 = {
    'owner_name': 'ganguli',
    'type_of_pet': ['cat'],
}

pet_1 = {
    'owner_name': 'john',
    'type_of_pet': ['dog'],
}

pet_2 = {
    'owner_name': 'curie',
    'type_of_pet': ['dog', 'cat'],
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"\n{pet['owner_name'].title()}'s favorite pets are:")
    for pet_info in pet['type_of_pet']:
        print(f"\t{pet_info.title()}")
