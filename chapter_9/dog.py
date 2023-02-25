class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simutate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simutate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over.")


# making a instance from a class
my_dog = Dog('Wille', 6)
# accessing attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
my_dog.roll_over()

# another instance
your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog's is {your_dog.age} years old.")
your_dog.sit()