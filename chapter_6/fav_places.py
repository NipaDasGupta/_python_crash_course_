''' Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person's name and their favorite places.'''

favorite_places = {
    'sarah': ['tokyo', 'maldive', 'paris'],
    'john': ['new york', 'bali', 'vitenam'],
    'nipa': ['paris', 'tokyo', 'maldive',],
}

for person, favorite_places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for favorite_place in favorite_places:
        print(f"\t{favorite_place.title()}")