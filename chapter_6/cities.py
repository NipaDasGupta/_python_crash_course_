'''Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city's dictionary should be something like
country, population, and fact. Print the name of each city and all of the
information you have stored about it.'''

cities = {
    'chittagong': {
        'country': 'bangladesh',
        'populations': 8_444_000,
        'fact': 'It is known for its rich biodiversity.',
    },

    'tokyo': {
        'country': 'japan',
        'populations': 13_960_000,
        'fact': "It is the world's most populous metropolitan area."
    },

    'paris': {
        'country': 'france',
        'populations': 2_140_000,
        'fact': "It has 5 statues of Liberty."
    },

}

for city, cities_info in cities.items():
    print(f"\n{city.title()}:")
    country = cities_info.get('country')
    populations = cities_info.get('populations')
    fact = cities_info.get('fact')
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulations: {populations}")
    print(f"\tFact: {fact}")