filename = 'chapter_10\\alice.txt'

# with open(filename) as f:
#     contents = f.read()
# print(contents)

# Handling the FileNotFoundError exception
try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the appoximate number of words in the file
    words = contents.split()
    num_words = len(words)
    # checking the data type of words
    print(type(words))
    print(f"The file {filename} has about {num_words} words.")