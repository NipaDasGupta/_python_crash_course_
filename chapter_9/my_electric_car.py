from electric_car import ElectricCar as EC

# Create a new instance of the ElectricCar
my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_decriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()
