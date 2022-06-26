class User:

    def __init__(self, _str_username):
        self.str_username = _str_username
        self.dct_passwords = {}

    def __len__(self):
        return len(self.dct_passwords)

    def __str__(self):
        locations = [k for k in self.dct_passwords.keys()]
        return f'User {self.str_username} is registered on locations {locations}.'

    def __getitem__(self, str_location):
        if str_location in self.dct_passwords:
            return self.dct_passwords[str_location]
        else:
            print(f'User {self.str_username} is not registered on location {str_location}.')
            return None

    def __setitem__(self, str_location, password):
        if str_location not in self.dct_passwords:
            self.dct_passwords[str_location] = password
        else:
            print(f'User {self.str_username} is already registered on location {str_location}.')

    def __delitem__(self, str_location):
        if str_location in self.dct_passwords:
            del self.dct_passwords[str_location]
        else:
            print(f'User {self.str_username} is not registered on location {str_location}.')

    def __iter__(self):
        return iter(self.dct_passwords.items())
