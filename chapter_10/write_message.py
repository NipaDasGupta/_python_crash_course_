filename = "chapter_10\\programming.txt"

# Writing to an empty file
with open(filename, 'w') as file_object:
    # Writing multiple lines
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    print("File has been upgraded!")

# Appending to a file
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")