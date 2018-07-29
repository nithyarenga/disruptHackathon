from bottle import route, run
from bottle import post, get, put, delete
from bottle import response, request
import requests
from json import dumps, loads
import json
import pusher
import threading
import time
import cPickle as pickle
import build_matrix

#ids
group_id="sid"
user_id="siddhukrs"

@get('/hello')
def hello():
    return "Hello World!"

@post('/images')
def images():
        value = request.body.read()
        v = loads(value)
        print v['user_id']
        print v['url']
        response.status = 200
        return {}

@post('/token')
def token():
    value = request.body.read()
    print value
    v = loads(value)
    if v.get('user_id') is None:
        response.status = 400
        return {"result": 400}
    else:
        user_id=v['user_id']
    if v.get('group_id') is None:
        response.status = 400
        return {"result": 400}
    else:
        group_id = v['group_id']
    if v.get('access_token') is None:
        response.status = 400
        return {"result": 400}
    else:
        access_token = v['access_token']
    response.status = 200
    thr = threading.Thread(target=gopis_method, args=(user_id, access_token, group_id), kwargs={})
    thr.start()
    return {"result": 200}

@post('/reco')
def reco():
    result = [{
        "url": "https://scontent.cdninstagram.com/vp/87c04d0814eb22217015f5d4757c5aeb/5C0D0AF2/t51.2885-15/sh0.08/e35/s640x640/37254209_2119495828322471_6795489576329674752_n.jpg?_nc_eui2=AeGwhmWbrK2upocXw-fitQ_XtU8urjdHJuMnzfaBnVJtH1BjmaHwo-8MG0W6gYuTM0xjfzRLQYNhSdmC_aJbxIbv",
        "location": "Austin",
        "description":["adventure" , "music" , "food"]
    },
    {
        "url": "https://scontent.cdninstagram.com/vp/9fb93cba53ad14819ff20b4044434721/5BF21B8A/t51.2885-15/sh0.08/e35/s640x640/36160470_1036318143194877_7432221918230478848_n.jpg?_nc_eui2=AeFuns6crQY85jwZFDPKqZai8z76-sZPK60lxUaYIpb-XENHpCHB2knRX6uxb7GnN-skGIm_o-ZcMT5tL-IQG4-I",
        "location": "Germany",
        "description":["hills" , "music" , "culture"]
    }
    ]

    # pkl_file = open('myfile.pkl', 'rb')
    # result = pickle.load(pkl_file)
    # pkl_file.close()
    
    push_sid(result)
    response.status = 200
    return {"result": 200}
    

def push_sid(urls):
    pusher_client = pusher.Pusher(
        app_id='562354',
        key='472deb41d62feac32b9b',
        secret='d804a3b8190eb2145459',
        cluster='us2',
        ssl=True
    )
    for url in urls:
        pusher_client.trigger(user_id,'prependEntryEvent',url)

def read_instagram_feed(user_id,access_token):
    url="https://api.instagram.com/v1/users/self/media/recent/?access_token="+access_token+"&count=20"
    r = requests.get(url)

    resp = json.loads(r.text)
    responseBody = {}
    responseBody["username"] = user_id
    responseBody["urls"] = []
    for post in resp["data"]:
        responseBody["urls"].append(post["images"]["standard_resolution"]["url"])
    # print "----------"
    # print responseBody
    return responseBody["urls"]

def gopis_method(user_id, access_token, group_id):
    
    # pkl_file = open('myfile.pkl', 'rb')
    # old_reco = pickle.load(pkl_file)

    # instagram_urls = read_instagram_feed(user_id, access_token)
    # new_reco=build_matrix.run_instagram_model(group_id, instagram_urls)
    # print new_reco
    # old_reco.append(new_reco)
    # pkl_file = open('myfile.pkl', 'wb')
    # mydict2 = pickle.dump(pkl_file)
    # push_sid(mydict2)

    
    result = [{
        "url": "https://scontent.cdninstagram.com/vp/87c04d0814eb22217015f5d4757c5aeb/5C0D0AF2/t51.2885-15/sh0.08/e35/s640x640/37254209_2119495828322471_6795489576329674752_n.jpg?_nc_eui2=AeGwhmWbrK2upocXw-fitQ_XtU8urjdHJuMnzfaBnVJtH1BjmaHwo-8MG0W6gYuTM0xjfzRLQYNhSdmC_aJbxIbv",
        "location": "Austin",
        "description":["adventure" , "music" , "food"]
    },
    {
        "url": "https://scontent.cdninstagram.com/vp/9fb93cba53ad14819ff20b4044434721/5BF21B8A/t51.2885-15/sh0.08/e35/s640x640/36160470_1036318143194877_7432221918230478848_n.jpg?_nc_eui2=AeFuns6crQY85jwZFDPKqZai8z76-sZPK60lxUaYIpb-XENHpCHB2knRX6uxb7GnN-skGIm_o-ZcMT5tL-IQG4-I",
        "location": "Germany",
        "description":["hills" , "music" , "culture"]
    }
    ]
    push_sid(result)


run(host='localhost', port=8080, debug=True)
#run(host='172.30.0.165', port=8080, debug=True)
