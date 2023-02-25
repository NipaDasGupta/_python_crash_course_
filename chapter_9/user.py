"""A class that can be used to represent a user."""

class User:
    """A simple attempt to build a user profile."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize first name, last name, age and email attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Describe a user information."""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"\nFull name: {full_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Greetings a user."""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello, {full_name}.")

    def read_login_attempts(self):
        """Read login attempts of the user."""
        print(f"User's login attempts: {self.login_attempts}")

    def increment_login_attempts(self):
        """Increment the user login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the user login attempts."""
        self.login_attempts = 0
