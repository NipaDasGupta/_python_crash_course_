def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


# make_pizza('pepporoni')
# make_pizza('pepporoni', 'pepporoni', 'extra cheese', 'green peppers')


def make_pizza1(*toppings):
    """Summarize the pizzaa we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# make_pizza1('pepporoni')
# make_pizza1('mushrooms', 'extra cheese', 'green peppers')


def make_pizza2(size, *toppings):
    """Summarize the pizzaa we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza2(12, 'pepporoni')
# make_pizza2(16, 'mushrooms', 'extra cheese', 'green peppers')