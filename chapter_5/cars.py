# a simple example
'''The following short example shows how if tests let you respond to special 
situations correctly. Imagine you have a list of cars and you want to print 
out the name of each car. Car names are proper names, so the names of 
most cars should be printed in title case. However, the value 'bmw' should 
be printed in all uppercase. The following code loops through a list of car 
names and looks for the value 'bmw'. Whenever the value is 'bmw', it's printed 
in uppercase instead of title case.'''
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if cars == 'bmw':
        print(car.upper())
    else:
        print(car.title())
