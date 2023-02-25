players = ['charles', 'martina', 'michael', 'florence', 'eli']

# slice a list
print(players[0:3])
print(players[:4])
print(players[1:4])
print(players[2:])
print(players[-3:])

# loop through a slice
for player in players[:3]:
    print(player.title())

