car = 'bmw'
# cheking for equality
# This is a equality operator sign (==).
if car == 'bmw':
    print(car == 'bmw')

car = 'audi'
if car == 'bmw':
    print(car == 'bmw')

# Ignoring Case When Checking for Equality
# Testing for equality is case sensitive in Python. For example, two values with 
# different capitalization are not considered equal
car = 'Audi'
if car == 'audi':
    print(False)

# convert the variable’s value to lowercase before doing the comparison 
# the test of varibale 'car' is now case insensitive
if car.lower() == 'audi':
    print(True)
