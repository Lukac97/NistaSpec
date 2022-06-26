import hash_module

def prompt_register():
    str_username = input("Please enter your username: ")

    str_password = ""
    while str_password == "" or len(str_password) > 15:
        str_password = input("Please enter your password: ")

    str_location = input("Please enter registering location: ")

    str_hashed_password = hash_module.hash_password(str_password)
