"""A class that can be used to represent an admin user."""
from user import User

class Privileges:
    """A simple attempt to represent a privilege of an admin user."""

    def __init__(self, *privileges):
        """Initialize the Priviledge's attributes."""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_priviledge(self):
        """Print a statement about the priviledge of the user."""
        print(f"\nThe admin priviledges are:\n{self.privileges}")


class Admin(User):
    """Represent aspects of a user, specific to admin user."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an admin user."""
        super().__init__(first_name, last_name, age, email)
        self.priviledges = Privileges()
