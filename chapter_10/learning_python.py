filename = 'chapter_10\\learning_python.txt'

# Reading an entire file
# with open(filename) as file_object:
#     contents = file_object.read()
# print(contents)

# Reading line by line
with open(filename) as file_object:
    for content in file_object:
        print(content.rstrip())

# Making a list of the lines from a file
# with open(filename) as file_object:
#     contents = file_object.readlines()

# for content in contents:
#     print(content.rstrip())
