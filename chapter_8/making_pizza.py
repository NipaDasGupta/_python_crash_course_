# import the whole module
# import pizza


# pizza.make_pizza2(12, 'pepporoni')
# pizza.make_pizza2(16, 'mushrooms', 'extra cheese', 'green peppers')


# Using as to give a module an alias
# import pizza as p


# p.make_pizza2(12, 'pepporoni')
# p.make_pizza2(16, 'mushrooms', 'extra cheese', 'green peppers')

# import specific functions
# from pizza import make_pizza2 as mp


# make_pizza2(12, 'pepporoni')
# make_pizza2(16, 'mushrooms', 'extra cheese', 'green peppers')


# Using as to give a function an alias
# from pizza import make_pizza2 as mp


# mp(12, 'pepporoni')
# mp(16, 'mushrooms', 'extra cheese', 'green peppers')

# importing all functions in a module
from pizza import *

make_pizza('pepporoni')
make_pizza1('pepporoni')
make_pizza2(16, 'mushrooms', 'extra cheese', 'green peppers')