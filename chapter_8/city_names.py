"""City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned."""


def get_city_names(city_name, country):
    """Return a city and its country name, neatly formatted."""
    formatted_city_name = f'"{city_name}, {country}"'
    return formatted_city_name.title()


print(get_city_names('santiago', 'chile'))
print(get_city_names('chittagong', 'bangladesh'))
print(get_city_names('paris', 'france'))


"""Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album's dictionary. Make at least
one new function call that includes the number of songs on an album."""


def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary describing a music album."""
    album = {
        'artist': artist_name,
        'album title': album_title
    }

    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

print(make_album('pink floyd', 'the dark side of the moon'))
print(make_album('ac/dc', 'back in black', 10))
print(make_album('bruce springteen', 'born to run', 200))

"""User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album's artist and title. Once you have that
information, call make_album() with the user's input and print the dictionary
that's created. Be sure to include a quit value in the while loop.
"""


while True:
    print("\nPlease tell me your favorite music album and artist name:")
    print("(enter 'q' at any time to quit)")

    a_name = input("\nArtist name: ")
    if a_name == "q":
        break

    alb_name = input("Album name: ")
    if alb_name == "q":
        break

    formatted_album = make_album(a_name, alb_name)
    print(f"\n--- Created a new album ---")
    print(formatted_album)