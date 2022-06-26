class User:

    def __init__(self, _str_username):
        self.str_username = _str_username
        self.dct_passwords = {}

    def mtd_add_location(self, str_new_location, str_hashed_pw):
        self.dct_passwords[str_new_location] = str_hashed_pw
