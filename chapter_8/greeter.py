# defining a function


def greet_user():
    """Display a simple greeting."""
    print("Hello!")


# function call
greet_user()

# passing information to a function


def greet_user1(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


# function call with arguments call 'nipa'


greet_user1("nipa")


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# This is a infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("\nFirst Name: ")
    if f_name == "q":
        break

    l_name = input("Last Name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


def get_formatted_name1(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# This is a infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("\nFirst Name: ")
    if f_name == "q":
        break

    m_name = input("Middle Name: ")
    if m_name == "q":
        break

    l_name = input("Last Name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name1(f_name, l_name, m_name)
    print(f"\nHello, {formatted_name}!")

