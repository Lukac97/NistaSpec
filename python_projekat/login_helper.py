import hash_module
from python_projekat.user_model import User
from python_projekat.register_helper import fct_get_user_by_name


def fct_check_login(obj_user, str_location, str_password):
    if obj_user[str_location] is not None:
        check_real_password = hash_module.check_password(
            obj_user[str_location], str_password)
        if check_real_password:
            print("Successful login")
        else:
            print("Unsuccessful login")
    else:
        print("Unsuccessful login")


def fct_prompt_login(obj_db):
    obj_user = None
    while obj_user is None:
        str_username = input("Please enter your username: ")
        obj_user = fct_get_user_by_name(obj_db, str_username)
        if obj_user is None:
            print("ERROR: "
                  "Username doesn't exist in database, try again.)")

    str_password = input("Please enter your password: ")
    str_location = input("Please enter password location: ")

    fct_check_login(obj_user, str_location, str_password)
