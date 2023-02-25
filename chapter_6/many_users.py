users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

for username, user_info in users.items():
    print(f"\nUsename: {username}")
    full_name = f"{user_info.get('first')} {user_info.get('last')}"
    location = f"{user_info.get('location')}"
    print(f"Full Name: {full_name.title()}")
    print(f"Location: {location.title()}")
