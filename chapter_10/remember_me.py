# Saving and reading user-generated information
import json

# username = input("What's your name? ")

# filename = 'chapter_10/username.json'
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f"We'll remember you when you come back, {username}!")


filename = 'chapter_10/username.json'


def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("\nWhat's your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    # Ask the user if this is the correct username or not.
    print(f"\nAre you {username}?")
    answer = input("Please, type 'y' or 'n': ")
    if answer == "y":
        print(f"\nWelcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


def main():
    """Run the main program."""
    greet_user()

if __name__ == "__main__":
    main()

