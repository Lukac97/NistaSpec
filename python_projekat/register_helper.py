import hash_module

from python_projekat.user_model import User


def fct_get_user_by_name(obj_db, str_username):
    # TODO: implement logic for getting user object from db.
    return obj_db.mtd_get_user_by_name(str_username)


def fct_create_new_user(obj_db, str_username):
    obj_user = User(str_username)
    obj_db.mtd_add_new_user(obj_user)
    return obj_user


def fct_prompt_register(obj_db):
    str_username = input("Please enter your username: ")
    obj_user = fct_get_user_by_name(obj_db, str_username)
    if obj_user is None:
        obj_user = fct_create_new_user(obj_db, str_username)

    str_password = ""
    while str_password == "" or len(str_password) > 15:
        str_password = input("Please enter your password: ")

    str_location = input("Please enter registering location: ")

    if str_location in obj_user.dct_passwords:
        print("This user is already registered on this location.")
    else:
        obj_user.mtd_add_location(
            str_location, hash_module.hash_password(str_password))