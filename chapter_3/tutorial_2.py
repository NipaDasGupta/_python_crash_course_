guests = ['priti', 'bikash', 'nicholas']

for guest in guests:
    print(f"Greetings, {guest.title()}! I would like to invite you in my dinner party.")
    print(f"Unfortunately, Bikash can't make it to dinner!")
    print()

guests[1] = 'trevor'
for guest in guests:
    print(f"Greetings, {guest.title()}! I would like to invite you in my dinner party.")
    print()

for guest in guests:
    print(f"Good news, {guest.title()}! I found a bigger dinner table.")
    print()

guests.insert(0, 'dipa')
guests.insert(1, 'fanilo')
guests.insert(-1, 'zuzana')

for guest in guests:
    print(f"Greetings, {guest.title()}! I would like to invite you in my dinner party.")
    print()

print(f"Number of guests are invited to dinner is {len(guests)}.")

for guest in guests:
        print(f"Sorry, {guests.pop()}! I can't invite you to my dinner party.")

print(f"Sorry, {guests.pop()}! I can't invite you to my dinner party.")
print()

for guest in guests:
    print(f"Greetings, {guest.title()}! I would like to invite you in my dinner party.")
    print()

del guests[0:]
print(guests)