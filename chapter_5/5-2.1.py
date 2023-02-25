admin_users = ['david', 'ada', 'nipa']
user = 'adam'
if 'ada' in admin_users:
    print("Grant!")

if user not in admin_users:
    print("Access denied!")