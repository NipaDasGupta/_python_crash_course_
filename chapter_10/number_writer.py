# Storing data using json.dump() to store data and json.load() to retrieve data.
import json

numbers = [2, 3, 4, 5, 6]

filename = 'chapter_10/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
