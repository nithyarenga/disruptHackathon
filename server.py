from bottle import route, run
from bottle import post, get, put, delete
from bottle import response, request
import requests
from json import dumps, loads
import json


group_id=""

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
    instagram_user_urls = read_instagram_feed(v['user_id'],v['access_token'])
    group_id = v['group_id']
    response.status = 200

    retry =  gopis_method(instagram_user_urls)
    return {"result": retry}


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

def gopis_method(instagram_urls):
    result = [{
        "image": "https://scontent.cdninstagram.com/vp/87c04d0814eb22217015f5d4757c5aeb/5C0D0AF2/t51.2885-15/sh0.08/e35/s640x640/37254209_2119495828322471_6795489576329674752_n.jpg?_nc_eui2=AeGwhmWbrK2upocXw-fitQ_XtU8urjdHJuMnzfaBnVJtH1BjmaHwo-8MG0W6gYuTM0xjfzRLQYNhSdmC_aJbxIbv",
        "location": "Austin",
        "tags":["adventure" , "music" , "food"]
    },
    {
        "image": "https://scontent.cdninstagram.com/vp/9fb93cba53ad14819ff20b4044434721/5BF21B8A/t51.2885-15/sh0.08/e35/s640x640/36160470_1036318143194877_7432221918230478848_n.jpg?_nc_eui2=AeFuns6crQY85jwZFDPKqZai8z76-sZPK60lxUaYIpb-XENHpCHB2knRX6uxb7GnN-skGIm_o-ZcMT5tL-IQG4-I",
        "location": "Austin",
        "tags":["adventure" , "music" , "food"]
    }
    ]
    return result


run(host='localhost', port=8080, debug=True)
