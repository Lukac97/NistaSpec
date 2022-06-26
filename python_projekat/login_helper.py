import time
import hash_module
from python_projekat.user_model import User
from python_projekat.register_helper import fct_get_user_by_name


def fct_prompt_login(obj_db):
    obj_user = None
    while obj_user is None:
        try:
            str_username = input("Please enter your username: ")
            obj_user = fct_get_user_by_name(obj_db, str_username)
        except Exception:
            print("ERROR: "
                  "Username doesn't exist in database, try again in 5s...)")
            time.sleep(5)
            continue
        break

    str_password = input("Please enter your password: ")
    str_location = input("Please enter password location: ")

    if str_location in obj_user.dct_passwords and obj_db.mtd_check_pass_exist(
            str_location, hash_module.hash_password(str_password)):
        str_hashed_password = hash_module.hash_password(str_password)
        check_real_password = hash_module.check_password(str_hashed_password,
                                                         str_password)
        if check_real_password:
            print("Successful login")
        else:
            print("Unsuccessful login")
    else:
        print("Wrong password or password location entered")
