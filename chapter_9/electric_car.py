"""A class that can be used to represent a electric car."""
from car import Car


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attribute."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement decribing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range of this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 0

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Print a statement about the upgraded battery."""
        if self.battery_size:
            self.battery_size = 100


class ElectricCar(Car):
    """Represent aspects of a car, specific to electical vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        # Instance as attribute
        self.battery = Battery()

    # Ovveriding methods from the parent class
    def fill_gas_tank(self):
        """Electric car don't have a gas tank."""
        print("This car does not need a gas tank!")
