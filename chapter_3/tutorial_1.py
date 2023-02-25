names = ['nicholas', 'trevor', 'zuzana', 'fanilo']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

message = "Greetings,"
print(f"{message} {names[0].title()}!")
print(f"{message} {names[1].title()}!")
print(f"{message} {names[2].title()}!")
print(f"{message} {names[3].title()}!")

motorcycles = ['Honda', 'Thunderbolt', 'Venom']

for motorcycle in motorcycles:
    print(f"I would like to own a {motorcycle} motorcycle.")