import json

filename = 'chapter_10/numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)