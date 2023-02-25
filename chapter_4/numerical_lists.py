"""class range(object)
    |  range(stop) -> range object
    |  range(start, stop[, step]) -> range object"""

help(range)

for value in range(5):
    print(value)

print('')

for value in range(1, 5):
    print(value)

print('')

print(type(range(5)))

numbers = list(range(1,6))
print(type(numbers))

even_numbers = list(range(2,11,2))
print(even_numbers)

# the square of each integer from 1 through 10
squares = []
for value in range(1,11):
    # exponent: **
    square = value ** 2
    squares.append(square)

for value in range(1, 11):
    squares.append(value**2)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)


