for value in range(1, 21):
    print(value)

number_list = list(range(1, 1_000_000))
for value in number_list:
    print(value)

print(min(number_list))
print(max(number_list))
print(sum(number_list))

for value in range(1, 20, 2):
    print(value)

multiples_numbers = [value for value in range(3, 31, 3)]
print(multiples_numbers)

cubes = [value**3 for value in range(1, 11)]
print(cubes)
