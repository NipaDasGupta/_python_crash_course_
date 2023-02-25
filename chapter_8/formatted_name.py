# returning a simple value
def get_formatted_value(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


engineer = get_formatted_value('nipa', "das gupta")
print(engineer)


def get_formatted_value(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_value('john', 'lee', 'hooker')
print(musician)


def get_formatted_value(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


engineer = get_formatted_value('nipa', "das gupta")
print(engineer)
musician = get_formatted_value('john', 'lee', 'hooker')
print(musician)
