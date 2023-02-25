# File path
filename = "chapter_10/pi_digits.txt"
filename = "chapter_10\\pi_million_digits.txt"

# Reading an entire file
# with open(filename) as file_object:
#     contents = file_object.read()
# print(contents)

# Reading an entire file
# with open(filename) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# Reading line by line
# with open(filename) as file_object:
#     for line in file_object:
#         print(line)

# Reading line by line
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# Making a list of the lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# checking the type of data
# print(type(lines))

# Working with a file's contents
# pi_string = ''
# for line in lines:
#     # get rid of right whitespaces
#     pi_string += line.rstrip()

# print(pi_string)
# print(len(pi_string))

# Working with a file's contents
pi_string = ''
for line in lines:
    # get rid of right and left whitespaces
    pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

# Large files: one millon digits
# Display the first 50 decimal places of Pi
# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# Is your birthday contained in Pi?
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first millon digits of Pi!")
else:
    print("Your birthday doesn't appears in the first millon digits of Pi!")
