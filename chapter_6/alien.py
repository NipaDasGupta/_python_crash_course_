# a simplest example of the dictionary
alien_0 = {"color": "green", "points": 5}

# adding values to the dictionary
print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

# adding new key-values pairs to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# starting with an empty dictionary
alien_0 = {}
alien_0['color'] = "green"
alien_0['points'] = 5
print(alien_0)

# modifying values in a dictionary
alien_0['color'] = "yellow"
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# modifying the 'speed' key in the dictionary
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3


alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

alien_0 = {"color": "green", "points": 5}
# removing key-value pairs
del alien_0['points']
print(alien_0)

