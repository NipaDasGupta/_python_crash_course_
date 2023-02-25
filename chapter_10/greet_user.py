import json

# # Load the username, if it has been stored previously
# filename = 'chapter_10/username.json'
# with open(filename) as f:
#     username = json.load(f)
# print(f"Welcome back, {username}!")


# Load the username, if it has been stored previously
# Otherwise, prompt for the username and store it
# filename = 'chapter_10/username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What's your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     print(f"We'll remember you when you come back, {username}!")
# else:
#     print(f"Welcome back, {username}!")
