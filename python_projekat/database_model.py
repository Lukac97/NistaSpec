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
