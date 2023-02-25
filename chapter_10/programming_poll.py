filename = "chapter_10\\poll_result.txt"

with open(filename, 'a') as file_object:
    file_object.write("Poll results:\n")
    while True:
        answer = input("Why do you like programming? ")
        if answer == "q":
            break
        else:
            print(f"Thanks for taking the poll!\n")
            file_object.write(f"- {answer}\n")
print("Poll completed!")
