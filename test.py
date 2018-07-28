import pusher
pusher_client = pusher.Pusher(
        app_id='562354',
        key='472deb41d62feac32b9b',
        secret='d804a3b8190eb2145459',
        cluster='us2',
        ssl=True
    )
r  = {
        "url": "https://scontent.cdninstagram.com/vp/a287b082191e1596b2d080b563d451cd/5BEFE52B/t51.2885-15/sh0.08/e35/s640x640/35574508_632940747059311_7646929446481428480_n.jpg?_nc_eui2=AeHi2joXR3BVxn19LdJygadHveAx10GhOj3CjV_i-1IDLf5qkHXbFINnDi7Vwva3d0rzvUTjNzaJIg-udCfRCT-_",
        "location": "Austin",
        "description":"adventure"
    }

pusher_client.trigger("siddhukrs",'prependEntryEvent',r)