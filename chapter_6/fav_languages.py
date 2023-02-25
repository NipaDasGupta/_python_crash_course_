# a dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# language = favorite_languages['nipa']
# print(language)

# Using get() to access values
language = favorite_languages.get('nipa', "Username is not available.")
print(language)

language = favorite_languages.get('nipa')
print(language)

# looping through all the key-values pairs in a dictionary
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through all the keys in a dictionary
for name in favorite_languages.keys():
    print(f"{name.title()}")

# likewise, looping through all the keys in a dictionary
for name in favorite_languages:
    print(f"{name.title()}")

friends = ['phil', 'sarah']
for name, language in favorite_languages.items():
    print(f"{name.title()}")

    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love {language.title()}.")

if 'erin' not in favorite_languages.keys():
    print(f"Erin, please take our poll!")

# looping through a dictionary's keys in a particular order
for name, language in sorted(favorite_languages.items()):
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through all the values in the dictionary
print("\nThe followning languages have been mentioned:")
for language in favorite_languages.values():
    print(f"{language.title()}")

"""To see each language chosen without repetition, we can use a set.
A set is a collection in which each item must be unique."""
print("\nThe followning languages have been mentioned without repetition:")
for language in set(favorite_languages.values()):
    print(f"{language.title()}")

# an example of set data type. You can build a set directly using braces and
# separating the elements with commas.
languages = {'python', 'c', 'ruby', 'python'}
print(languages)

'''Use the code in favorite_languages.py (page 97).
•	 Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
'''

poll_request = ['nipa', 'phil', 'sarah', 'andrew']
for name in favorite_languages:
    if name not in poll_request:
        print('Please take the poll!')
    else:
        print(f'{name.title()}, thanks for taking the poll!')

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")