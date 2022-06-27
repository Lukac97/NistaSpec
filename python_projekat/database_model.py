import json

from python_projekat.user_model import User


class Database:
    def __init__(self):
        self.lst_users = []

    def mtd_get_user_by_name(self, str_name):
        for obj_user in self.lst_users:
            if obj_user.str_username == str_name:
                return obj_user

        return None

    def mtd_add_new_user(self, obj_user):
        self.lst_users.append(obj_user)

    def mtd_load_model(self):
        with open("username_database.json", 'r') as f:
            dict_users = json.load(f)

        self.lst_users = []

        for user in dict_users["username_and_passwords"]:
            obj_data = User(user["username"])
            obj_data.dct_passwords= user["passwords"]
            self.lst_users.append(obj_data)

    def mtd_write_new_user_in_model(self):
        dict_users = {
            "usernames_and_passwords": []
        }

        for user in self.lst_users:
            dict_user = {
                "username": user.str_username,
                "passwords": user.dct_passwords
            }

        with open("username_database.json", 'w') as f:
            json.dump(dict_users, f)
