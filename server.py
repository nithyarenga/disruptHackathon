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
import os.path


mock_results = [{
        "url": ["https://scontent.cdninstagram.com/vp/87c04d0814eb22217015f5d4757c5aeb/5C0D0AF2/t51.2885-15/sh0.08/e35/s640x640/37254209_2119495828322471_6795489576329674752_n.jpg?_nc_eui2=AeGwhmWbrK2upocXw-fitQ_XtU8urjdHJuMnzfaBnVJtH1BjmaHwo-8MG0W6gYuTM0xjfzRLQYNhSdmC_aJbxIbv" ,"https://scontent.cdninstagram.com/vp/87c04d0814eb22217015f5d4757c5aeb/5C0D0AF2/t51.2885-15/sh0.08/e35/s640x640/37254209_2119495828322471_6795489576329674752_n.jpg?_nc_eui2=AeGwhmWbrK2upocXw-fitQ_XtU8urjdHJuMnzfaBnVJtH1BjmaHwo-8MG0W6gYuTM0xjfzRLQYNhSdmC_aJbxIbv"],
        "location": "Austin",
        "description":["adventure" , "music" , "food"]
    },
    {
        "url": ["https://scontent.cdninstagram.com/vp/9fb93cba53ad14819ff20b4044434721/5BF21B8A/t51.2885-15/sh0.08/e35/s640x640/36160470_1036318143194877_7432221918230478848_n.jpg?_nc_eui2=AeFuns6crQY85jwZFDPKqZai8z76-sZPK60lxUaYIpb-XENHpCHB2knRX6uxb7GnN-skGIm_o-ZcMT5tL-IQG4-I" , "https://scontent.cdninstagram.com/vp/9fb93cba53ad14819ff20b4044434721/5BF21B8A/t51.2885-15/sh0.08/e35/s640x640/36160470_1036318143194877_7432221918230478848_n.jpg?_nc_eui2=AeFuns6crQY85jwZFDPKqZai8z76-sZPK60lxUaYIpb-XENHpCHB2knRX6uxb7GnN-skGIm_o-ZcMT5tL-IQG4-I"],
        "location": "Germany",
        "description":["hills" , "music" , "culture"]
    }
    ]

@get('/hello')
def hello():
    return "Hello World!"

# @post('/images')
# def images():
#         value = request.body.read()
#         v = loads(value)
#         #print v['user_id']
#         #print v['url']
#         response.status = 200
#         return {}

@post('/token')
def token():
    value = request.body.read()
    #print value
    v = loads(value)
    if v.get('user_id') is None:
        response.status = 400
        return {"result": 400}
    else:
        user_id=v['user_id']
        print user_id
    if v.get('group_id') is None:
        response.status = 400
        return {"result": 400}
    else:
        group_id = v['group_id']
        print group_id
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
    # result = mock_results
    value = request.body.read()
    #print value
    v = loads(value)
    if v.get('user_id') is None:
        response.status = 400
        return {"result": 400}
    else:
        user_id=v['user_id']
    file_name = group_id+".pkl"
    if os.path.isfile(file_name): 
        pkl_file = open(file_name, 'rb')
        result = pickle.load(pkl_file)
        pkl_file.close()
    else:
        result = mock_results
    push_sid(result, user_id)
    response.status = 200
    return {"result": 200}
    

def push_sid(urls, user_id):
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
    
    instagram_urls = read_instagram_feed(user_id, access_token)
    top_cities, top_cities_images, top_city_concepts=build_matrix.run_instagram_model(group_id, instagram_urls)
    # print top_cities
    # print "\n"
    # print top_cities_images
    # print "\n"
    # print top_city_concepts

    new_reco = []
    city_list = top_cities.most_common(4)
    for x in city_list:
        loc = x[0]
        new_json = {
            "location": loc,
            "url": [top_cities_images[loc][0],top_cities_images[loc][1],top_cities_images[loc][2]],
            "description": [top_city_concepts[loc][0],top_city_concepts[loc][1],top_city_concepts[loc][2]]
        }
        new_reco.append(new_json)

    file_name = group_id+".pkl"
    if not os.path.isfile(file_name): 
        file = open(file_name, 'w+')
        file.close()
        pkl_file = open(file_name, 'wb')
        pickle.dump(new_reco, pkl_file)
        pkl_file.close()
        push_sid(new_reco, user_id)
    else:
        pkl_file = open(file_name, 'rb')
        old_reco = pickle.load(pkl_file)
        pkl_file.close()
        new_reco.extend(old_reco)
        unique_reco = {v['location']:v for v in old_reco}.values()
        pkl_file = open(file_name, 'wb')
        pickle.dump(unique_reco, pkl_file)
        pkl_file.close()
        push_sid(unique_reco, user_id)


run(host='localhost', port=8080, debug=True)
#run(host='172.30.0.165', port=8080, debug=True)
