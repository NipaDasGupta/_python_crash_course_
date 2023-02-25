# how the input() function works
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# message = ""
# while message != 'quit':
#     message = input(prompt)
#    ! if message == 'quit', then the program will ignore the print message
#     if message != 'quit':
#         print(message)

# Using a flag
"""Let's add a flag to parrot.py from the previous section. This flag, which
we'll call active (though you can call it anything), will monitor whether or
not the program should continue running"""

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
