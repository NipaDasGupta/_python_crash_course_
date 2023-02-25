# looping through all key-value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for k,v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")
