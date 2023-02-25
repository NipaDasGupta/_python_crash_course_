# a list in a dictionary

# store the information about the pizza being ordered
pizza = {
    'crust': 'thick',
    'topping': ['mushrooms', 'extra cheese'],
}

# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following topping:")
for topping in pizza['topping']:
    print(f"\t{topping}")
