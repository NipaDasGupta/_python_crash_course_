def get_formatted_string(city, country, population=None):
    """Generate a neatly formatted city and capital name."""
    if population:
        formatted_string = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string