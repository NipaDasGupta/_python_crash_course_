bicycles = ['trek', 'cannon-dale', 'redline', 'specialized']
print(bicycles)

# #first element from the list
print(bicycles[0])
# #last element from the list
print(bicycles[-1])

print(bicycles[-1].title())

message = f"My first bicycle was a {bicycles[2].upper()}"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# how to get information about a function
help(motorcycles.remove)

# modify an element in a list
motorcycles[0] = 'ducati'
print(motorcycles)

# adding element in a list using append() method
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
print(motorcycles)

motorcycles.append("honda")
motorcycles.append('yamaha')
motorcycles.append("suzuki")
print(motorcycles)

# insert element in a list
motorcycles.insert(1, "ducati")
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# remove an element using del statement
del motorcycles[0]
print(motorcycles)

# remove an element using pop() method
print(motorcycles.pop())
print(motorcycles)

# print the length of a list
print(len(motorcycles))

# remove an element by value
motorcycles.remove('ducati')
print(motorcycles)

# sorting a list permanently with the sort() method
cars = ['tesla', "bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

# sort reverse alphabetical order by passing reverse=Ture
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily with the sorted() method
cars = ['tesla', "bmw", "audi", "toyota", "subaru"]
print(sorted(cars))
print(cars) # doesn't affect the original order

# print a list in reverse order
cars.reverse()
print(cars)

# IndexError: list index out of range
cars = ['tesla', "bmw", "audi", "toyota", "subaru"]
print(cars[5])
print(cars[-1])

# IndexError: list index out of range
motorcycles = []
print(motorcycles[-1])
print(motorcycles)