# import dependencies
from user import User
from admin import Admin

nipa = User('nipa', 'das gupta', 24, 'nipantika.nipa@gmail.com')
nipa.describe_user()
# nipa.greet_user()

admin = Admin('ada', 'lovelace', 33, 'ada33@gmail.com')
admin.describe_user()
admin.priviledges.show_priviledge()

# nipa.increment_login_attempts()
# nipa.increment_login_attempts()
# nipa.read_login_attempts()

# # reset the user login attempts
# nipa.reset_login_attempts()
# nipa.read_login_attempts()

# ada = User('ada', 'lovelace', 33, 'lovelace22@gmail.com')
# ada.describe_user()
# ada.greet_user()
