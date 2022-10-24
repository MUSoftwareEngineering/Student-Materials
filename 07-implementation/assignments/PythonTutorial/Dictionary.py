# Simple Dictionary
fav_colors = {

    'calebheinzman': 'green',
    'koltonspeer': 'red'
}
print(fav_colors['calebheinzman'])
print(fav_colors['koltonspeer'])

#Adding to a dictionary
fav_colors['seangoggins'] = 'purple'
print(fav_colors['seangoggins'])

#Dictionary of dictionary
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
print(users['calebheinzman']['fav_drink'])
print(users['koltonspeer']['fav_drink'])

