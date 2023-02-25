"""A class that can be used to represent a car."""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # setting a default value for an attribute
        self.odometer_reading = 0

    def get_decriptive_name(self):
        """Return a neatly formatted decriptive name."""
        long_name = f"{self.year} {self.make.title()} {self.model.title()}"
        return long_name

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("You can't add miles backward an odometer!")
        else:
            self.odometer_reading += miles
