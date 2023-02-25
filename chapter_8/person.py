def build_person(first_name, last_name):
    """Returns a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name,
    }
    return person


print(build_person('ada', 'lovelace'))
print()


def build_person1(first_name, last_name, age=None):
    """Returns a dictionary of information about a person."""
    person = {
        'first': first_name,
        'last': last_name,
    }
    if age:
        person['age'] = age
    return person


coder = build_person1('ada', 'lovelace', 30)
# looping through all key-value pairs
for key, value in coder.items():
    print(f"{key}: {value}")
