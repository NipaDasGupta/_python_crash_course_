"""Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let;s call it a glossary.
•	 Think of five programming words you've learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output."""

glossary = {
    'dictionary': 'A dictionary in Python is a collection of key-value pairs.',
    'key': 'Each key is connected to a value, and you can use a key to access the value associated with that key.',
    'value': 'A value can be a number, a string, a list, or even another dictionary.',
    'set': 'A set is a collection in which each item must be unique.',
    'sorted': 'A built-in method to sorted data temporarily.',
}

print(f"Dictionary: \n{glossary['dictionary']}\n")
print(f"Key: \n{glossary['key']}\n")
print(f"Value: \n{glossary['value']}\n")
print(f"Set: \n{glossary['set']}\n")
print(f"Sorted: \n{glossary['sorted']}\n")


'''Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary's keys and values. When
you're sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.'''

for key, value in glossary.items():
    print(f"\n{key.title()}:")
    print(f"{value}")
