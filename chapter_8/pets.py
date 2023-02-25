# postional arguments
def describe_pets(animal_type, pet_name):
    """Display information about pets."""
    print(f"\nI've a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# multiple function calls
describe_pets('dog', 'willie')
describe_pets('hamster', 'harry')

# order matters in postional arguments
describe_pets('harry', 'hamster')

# keyword arguments: it's a name-value pair that you pass to a function.
describe_pets(animal_type='hamster', pet_name='harry')
# the order of the keyword arguments doesn't matter
describe_pets(pet_name='harry', animal_type='hamster')


# default value
def alt_describe_pets(pet_name, animal_type='dog'):
    """Display information about pets."""
    print(f"\nI've a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


alt_describe_pets('willie')
describe_pets(pet_name='harry', animal_type='hamster')

# equivalent function calls
# a dog named 'willie'
alt_describe_pets('willie')
alt_describe_pets(pet_name='willie')

# A hamster named 'harry'
alt_describe_pets('harry', 'hamster')
alt_describe_pets(pet_name='harry', animal_type='hamster')
alt_describe_pets(animal_type='hamster', pet_name='harry')

# avioding arguments errors
alt_describe_pets()
