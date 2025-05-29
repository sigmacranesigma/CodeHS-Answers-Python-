def greeting(user_info):
    user_info = user_info.split()
    string = 'Hello, {user_info[0]}! I also enjoy {user_info[2]}!'
    return string.format(user_info=user_info)
