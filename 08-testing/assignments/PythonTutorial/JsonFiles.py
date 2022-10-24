import json

users = {
    'calebheinzman': {
        'password': '1234',
        'fav_color': 'green',
        'fav_drink': 'beer'

    },
    'koltonspeer': {
        'password': '420',
        'fav_color': 'red',
        'fav_drink': 'orange juice'
    },
}
with open('users.json', 'w') as fp:
    json.dump(users, fp)

with open('users.json') as f:
    users2 = json.load(f)

print(users2)