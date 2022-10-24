import json


class User:

    def update_user_db(self):
        with open('Data/users.json', 'w') as fp:
            json.dump(self.users, fp)
