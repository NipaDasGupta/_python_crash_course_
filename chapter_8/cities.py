"""Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in
the default country."""


def describe_city(city, country='iceland'):
    """Display the name of a city and its country.

    Args:
        city (str): Name of the city.
        country (str, optional): Name of its country. Defaults to 'iceland'.
    """
    print(f"\n{city.title()} is in {country.title()}.")


describe_city('reyjavik')
describe_city('tokyo')
describe_city(city='paris', country='france')
