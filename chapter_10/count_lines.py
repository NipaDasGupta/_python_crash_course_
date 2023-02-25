# Working with multiple files
def count_line(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        word = 'the '
        # Count the appoximate number of time a word appears in the file
        # line = contents.count(word)
        # Convert the string to lowercase using lower() method
        line = contents.lower().count(word)
        print(f"The word '{word}' has appeared about {line} times.")


filename = 'chapter_10\\alice.txt'
count_line(filename)