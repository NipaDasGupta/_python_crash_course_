import json

def get_stored_number():
    """Get stored favorite number if available."""
    filename = 'chapter_10/favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def get_new_number():
    """Prompt for a new favorite_number."""
    favorite_number = input("What's your favorite number? ")
    filename = 'chapter_10/favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number


def tell_favorite_number():
    """Greet the user by name."""
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = get_new_number()


tell_favorite_number()