def get_formatted_string(city, country, population=None):
    """Generate a neatly formatted information about a city."""
    if population:
        formatted_string = f"{city.title()}, {country.title()}. Population is {population}."
    else:
        formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string
