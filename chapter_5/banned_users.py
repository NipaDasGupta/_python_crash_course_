"""Checking Whether a Value Is Not in a List:
Other times, it's important to know if a value does not appear in a list. You 
can use the keyword 'not' in this situation. For example, consider a list of users 
who are banned from commenting in a forum. You can check whether a 
user has been banned before allowing that person to submit a comment"""

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

"""Boolean Expressions:
As you learn more about programming, you'll hear the term Boolean 
expression at some point. A Boolean expression is just another name for a 
conditional test. A Boolean value is either True or False, just like the 
value of a conditional expression after it has been evaluated.
Boolean values are often used to keep track of certain conditions, such 
as whether a game is running or whether a user can edit certain content on 
a website"""

game_active = True
can_edit = False
