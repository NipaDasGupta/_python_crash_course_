"""A class that can be used to represent a restaurant."""

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cusinine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cusinine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe a restaurant information."""
        print(
            f"\nThe {self.restaurant_name} serves {self.cuisine_type} cusinine.")

    def open_restaurant(self):
        """Display the restaurant is opened or not."""
        print(f"The restaurant is open.")

    def read_number_served(self):
        """Print a statement showing the number of customers served."""
        print(f"The restaurant has served {self.number_served} customers.")

    def set_number_served(self, customers_served):
        """Set the number of customers served."""
        if customers_served >= self.number_served:
            self.number_served = customers_served
        else:
            print(f"You cannot update the number of customers served.")

    def increment_number_served(self, served):
        """Add the given amount to read the number of customers served."""
        if served < 0:
            print(f"You cannot add the given amount to the served number.")
        else:
            self.number_served += served
