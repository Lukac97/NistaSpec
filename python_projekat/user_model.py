class User:

    def __init__(self, _str_username):
        self.str_username = _str_username
        self.dct_passwords = {}

    def mtd_add_location(self, str_new_location, str_hashed_pw):
        self.dct_passwords[str_new_location] = str_hashed_pw

    def mtd_check_pass_exist(self, str_location, str_hashed_pw):
        if self.dct_passwords[str_location] == str_hashed_pw:
            return True
        return False
