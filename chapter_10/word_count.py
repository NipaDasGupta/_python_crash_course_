# Working with multiple files
# def count_word(filename):
#     try:
#         with open(filename, encoding="utf-8") as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} does not exist.")
#     else:
#         # Count the appoximate number of words in the file
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")


# # filename = 'chapter_10/alice.txt'
# # count_word(filename)

# # counting number of words for list of files
# filenames = ['chapter_10/alice.txt', 'chapter_10/little_women.txt', 'chapter_10/nipa.txt', 'chapter_10/moby_dick.txt']
# for filename in filenames:
#     count_word(filename)


# Failing silently
def count_word_1(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        # Count the appoximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


# counting number of words for list of files
filenames = ['chapter_10/alice.txt', 'chapter_10/little_women.txt', 'chapter_10/nipa.txt', 'chapter_10/moby_dick.txt']
for filename in filenames:
    count_word_1(filename)
