'''Hello Admin: Make a list of five or more usernames, including the name 
'admin'. Imagine you are writing code that will print a greeting to each user 
after they log in to a website. Loop through the list, and print a greeting to 
each user:
•	 If the username is 'admin', print a special greeting, such as Hello admin, 
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Jaden, thank you for 
logging in again.'''

usernames = ['nipa', 'admin', 'jaden']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")

"""No Users: Add an if test to hello_admin.py to make sure the list of users is 
not empty.
•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct 
message is printed."""

usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print('We need to find some users!')

"""Checking Usernames: Do the following to create a program that simulates 
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or 
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already 
been used. If it has, print a message that the person will need to enter a 
new username. If a username has not been used, print a message saying 
that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used, 
'JOHN' should not be accepted. (To do this, you'll need to make a copy of 
current_users containing the lowercase versions of all existing users.)"""

current_users = ['Nipa', 'Admin', 'Jaden', 'Elevan', 'Sheldon']
new_users = ['nipa', 'Emily', 'Jaden', 'Pero', 'Gabrial']

for new_users in new_users:
    if new_users.title() in current_users:
        print(f"{new_users.title()} is taken! Please, enter a new username.")
    else:
        print(f"{new_users.title()} is avilable.")


'''Checking Usernames: Do the following to create a program that simulates 
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or 
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already 
been used. If it has, print a message that the person will need to enter a 
new username. If a username has not been used, print a message saying 
that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used, 
'JOHN' should not be accepted. (To do this, you'll need to make a copy of 
current_users containing the lowercase versions of all existing users.)
'''

for ordinary_number in range(1, 10):
    if ordinary_number == 1:
        print(f"{ordinary_number}st")
    elif ordinary_number == 2:
        print(f"{ordinary_number}nd")
    elif ordinary_number == 3:
        print(f"{ordinary_number}rd")
    else:
        print(f"{ordinary_number}th")
