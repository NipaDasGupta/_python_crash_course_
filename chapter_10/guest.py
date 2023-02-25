# filename = "chapter_10\\guest.txt"

# with open(filename, 'a') as file_object:
#     name = input("Please, enter your name? ")
#     file_object.write(f"{name}\n")
# print("File upgraded!")

filename = "chapter_10\\guest_book.txt"

with open(filename, 'a') as file_object:
    file_object.write("Guest book record:\n")
    while True:
        name = input("Please, enter your name? ")
        if name == 'q':
            break
        else:
            print(f"Hello, {name}!\n")
        file_object.write(f"- {name}\n")
print("File upgraded!")
