# Importing dependencies
from car import Car
from electric_car import ElectricCar as EC


my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_decriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_decriptive_name())

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_decriptive_name())

# modifying an attribute's value directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# modifying an attribute's value through an method
# my_new_car.update_odometer(23_000)
# my_new_car.read_odometer()

# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()