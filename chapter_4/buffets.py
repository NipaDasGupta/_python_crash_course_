'''Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
simple foods, and store them in a tuple.
•	 Use a for loop to print each food the restaurant offers.
•	 Try to modify one of the items, and make sure that Python rejects the 
change.
•	 The restaurant changes its menu, replacing two of the items with different 
foods. Add a line that rewrites the tuple, and then use a for loop to print 
each of the items on the revised menu.'''
buffet_foods = ('rice', 'fried chicken', 'boiled egg', 'veggie', 'potato curry')
print('Original buffet foods:')
for food in buffet_foods:
    print(food)

# buffet_foods[0]='fried rice'
# print(buffet_foods)
print('\n')

buffet_foods = ('fried rice', 'fried chicken', 'fried egg', 'veggie', 'potato curry')
print('Modified buffet foods:')
for food in buffet_foods:
    print(food)