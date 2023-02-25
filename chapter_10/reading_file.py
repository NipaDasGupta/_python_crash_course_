filename = "chapter_10\\learning_python.txt"

# # reading the entire file
# with open(filename) as file_object:
#     contents = file_object.read()
# print(contents)

# # looping over the file object
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# storing the lines in a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    # Replace the word 'Python' with 'C' in the file
    line = line.replace('Python', 'C')
    print(line.rstrip())
